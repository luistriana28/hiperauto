# -*- encoding: utf-8 -*-
from osv import osv, fields
from datetime import datetime

class fleet_vehicle_year(osv.osv):
    _name = 'fleet.vehicle'
    _inherit = 'fleet.vehicle'
    _columns = {
                'modelo':fields.selection([(num, str(num)) for num in range(1960, (datetime.now().year)+1 )], 'Modelo'),
        }
fleet_vehicle_year()