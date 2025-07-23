######
#manifest has data files,security files, demo files, depends arrays,name and summary,license
######

{
    "name":"first project",
    "summary":"testing project in odoo",
    "version":"0.1",
    "license":"GPL-3",
    "depends":["crm"],
    "data":[
        #security
            #books
                "security/access.xml",
            #model_a_many_2_one model_b_many_2_one
                "security/model_a_many_2_one_access.xml",
                "security/model_b_many_2_one_access.xml",
            #model_a_one_2_many model_b_one_2_many
                "security/model_a_one_2_many_access.xml",
                "security/model_b_one_2_many_access.xml",
            #model_a_many_2_many model_b_many_2_many
                "security/model_a_many_2_many_access.xml",
                "security/model_b_many_2_many_access.xml",
            
            "security/ir.model.access.csv",
        #views
            #books
                "views/books_properties_views.xml",
                "views/books_menus.xml", 
            #model_a_many_2_one model_b_many_2_one
                "views/model_a_many_2_one_views.xml",
                "views/model_a_many_2_one_menus.xml",
                "views/model_b_many_2_one_views.xml",
                "views/model_b_many_2_one_menus.xml",
            #model_a_one_2_many model_b_one_2_many
                "views/model_a_one_2_many_views.xml",
                "views/model_a_one_2_many_menus.xml",
                "views/model_b_one_2_many_views.xml",
                "views/model_b_one_2_many_menus.xml",
            #model_a_many_2_many model_b_many_2_many
                "views/model_a_many_2_many_views.xml",
                "views/model_a_many_2_many_menus.xml",
                "views/model_b_many_2_many_views.xml",
                "views/model_b_many_2_many_menus.xml",
    ],
    "demo":[
        "demo/demo.xml"
    ]
}