{
    "name": "first project",
    "summary": "testing project in odoo",
    "version": "0.1",
    "license": "GPL-3",
    "depends": ["crm"],
    "data": [
        #security
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        #views
        "views/real_estate_views.xml",
        "views/estate_type_views.xml",
        "views/estate_tag_views.xml",
        "views/estate_offer_views.xml",
        #menus
        "views/estate_menus.xml",
        
    ],
    "demo": [
        "demo/demo.xml",
    ],      
    "installable": True,
    "application": True
}
