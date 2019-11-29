{
    "name": "Taller Mecánico",
    "version": "1.0",
    "description":
    """
        This module add vehicle_id fleet field to sale order
    """,
    "author": "JARSA Sistemas, S.A. de C.V.",
    "depends": [
        "sale_stock",
        "fleet",
        "purchase"
    ],
    "data": [
        'views/taller_mecanico_view.xml',
        'views/taller_vehicle_view.xml',
        ],
    "demo_xml": [],
    "update_xml": [],
    "installable": True,
}
