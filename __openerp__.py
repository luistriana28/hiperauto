# -*- encoding: utf-8 -*-

{
    "name": "Taller Mecánico",
    "version": "1.0",
    "description":
    """
        Agrega campos al pedido de ventas, adaptado a un taller mecánico
        Tiene dependencias que se descargan en

        bzr branch lp:sale-reports

        bzr branch lp:webkit-utils/7.0
    """,
    "author": "JARSA Sistemas, S.A. de C.V.",
    "website": "http://www.marsistemas.com",
    "category": "Sales",
    "depends": ["sale_stock",
                "fleet",
                "sale_order_webkit",
                "purchase"],
    "data": ['views/taller_mecanico_view.xml',
             'views/taller_vehicle_view.xml',
             'views/taller_shop_view.xml',
             'security/taller_security.xml'],
    "demo_xml": [],
    "update_xml": [],
    "active": False,
    "installable": True,
    "certificate": "",
}
