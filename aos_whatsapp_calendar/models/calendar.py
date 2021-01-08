# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import api, fields, models, _
from odoo.addons.mail.models.mail_template import format_tz
import pytz
import datetime
from datetime import datetime

_logger = logging.getLogger(__name__)


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    def _get_default_whatsapp_recipients(self):
        """ Method overriden from mail.thread (defined in the sms module).
            SMS text messages will be sent to attendees that haven't declined the event(s).
        """
        return self.mapped('attendee_ids').filtered(lambda att: att.state != 'declined').mapped('partner_id')

    def _do_whatsapp_reminder(self):
        """ Send an SMS text reminder to attendees that haven't declined the event """
        for event in self:
            tz = pytz.timezone(event.user_id.tz)
            start_datetime = pytz.utc.localize(event.start_datetime).astimezone(tz)
            whatsapp_msg = _("Calendar Reminder: *%s* on %s") % (event.name, str(start_datetime.strftime("%d %b %Y %H:%M %p")) or event.start_date)
            if event.location:
                whatsapp_msg = whatsapp_msg + _(" at Location *%s*" % (event.location or ''))
            note_msg = _('Whatsapp text message reminder sent !')
            event.message_post_send_whatsapp(whatsapp_msg, note_msg=note_msg)


class CalendarAlarm(models.Model):
    _inherit = 'calendar.alarm'

    type = fields.Selection(selection_add=[('whatsapp', 'Whatsapp Text Message')])


class AlarmManager(models.AbstractModel):
    _inherit = 'calendar.alarm_manager'

    @api.model
    def get_next_mail(self):
        #print ("""===Cron method, overriden here to send Whatsapp reminders as well==""")
        result = super(AlarmManager, self).get_next_mail()
        now = fields.Datetime.to_string(fields.Datetime.now())
        last_whatsapp_cron = self.env['ir.config_parameter'].get_param('aos_whatsapp_calendar.last_whatsapp_cron', default=now)
        cron = self.env['ir.model.data'].get_object('calendar', 'ir_cron_scheduler_alarm')

        interval_to_second = {
            "weeks": 7 * 24 * 60 * 60,
            "days": 24 * 60 * 60,
            "hours": 60 * 60,
            "minutes": 60,
            "seconds": 1
        }
        cron_interval = cron.interval_number * interval_to_second[cron.interval_type]
        events_data = self.get_next_potential_limit_alarm('whatsapp', seconds=cron_interval)

        for event in self.env['calendar.event'].browse(events_data):
            max_delta = events_data[event.id]['max_duration']

            if event.recurrency:
                found = False
                for event_start in event._get_recurrent_date_by_event():
                    event_start = event_start.replace(tzinfo=None)
                    last_found = self.do_check_alarm_for_one_date(event_start, event, max_delta, 0, 'whatsapp', after=last_whatsapp_cron, missing=True)
                    for alert in last_found:
                        event.browse(alert['event_id'])._do_whatsapp_reminder()
                        found = True
                    if found and not last_found:  # if the precedent event had an alarm but not this one, we can stop the search for this event
                        break
            else:
                event_start = fields.Datetime.from_string(event.start)
                for alert in self.do_check_alarm_for_one_date(event_start, event, max_delta, 0, 'whatsapp', after=last_whatsapp_cron, missing=True):
                    event.browse(alert['event_id'])._do_whatsapp_reminder()
        self.env['ir.config_parameter'].set_param('aos_whatsapp_calendar.last_whatsapp_cron', now)
        return result
