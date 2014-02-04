# -*- encoding: utf-8 -*-
from osv import osv, fields

class sale_order(osv.osv):
    _name = 'sale.order'
    _inherit = 'sale.order'
    _columns = {
                'vehicle_id':fields.many2one('fleet.vehicle', 'Vehículo'),
                'antena': fields.boolean('Antena'),
                'autoestereo': fields.boolean('Autoestéreo'),
                'birlo': fields.boolean('Birlo de seguridad'),
                'pasacorriente': fields.boolean('Cables pasacorriente'),
                'espejos_laterales': fields.boolean('Espejos laterales'),
                'refaccion': fields.boolean('Llanta de refacción'),
                'maneral': fields.boolean('Llave o maneral'),
                'radio': fields.boolean('Radio de comunicación'),
                'senales': fields.boolean('Señales'),
                'tapetes': fields.boolean('Tapetes'),
                'extinguidor': fields.boolean('Extinguidor'),
                'gato': fields.boolean('Gato'),
                'herramienta': fields.boolean('Herramienta'),
                'limpiadores': fields.boolean('Limpiadores'),
                'tapon_gasolina': fields.boolean('Tapon de gasolina'),
                'tapon_ruedas': fields.boolean('Tapon de ruedas'),
                'nivel_combustible': fields.selection((('lleno','Tanque lleno'),('3/4','3/4'),('1/2','1/2'),('1/4','1/4'),('vacio','Vacío')),'Nivel de combustible'),
                'otro': fields.char('Otro',size=40),
        }
sale_order()