{
    "name":"testing_03",
    "sumarry":"odoo_advanced",
    "version":"1.0",
    "license":"LGPL-3",
    "depends":[],
    "data":[
        #security
                #employee
                "security/employee_access.xml",
                #test_candidat
                "security/test_candidat_access.xml",
            "security/ir.model.access.csv",
        #views
            #employee
                "views/employee_views.xml",
                "views/employee_menus.xml",
            #test_candidat
                "views/test_candidat_views.xml",
                "views/test_candidat_menus.xml",
            

    ],
    "demo":[],
    "assets":{}
}