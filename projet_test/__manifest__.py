{
    "name":"testing_01",
    "summary":"testing in odoo this project0001",
    "version":"0.1",
    "license":"LGPL-3",
    "depends":[],
    "data":[
        #security
            #first_test_model
                "security/first_test_model_access.xml",
            #model_a_many_2_one model_b_many_2_one
                "security/model_a_many_2_one_access.xml",
                "security/model_b_many_2_one_access.xml",
            #model_a_one_2_many model_b_one_2_many
                "security/model_a_one_2_many_access.xml",
                "security/model_b_one_2_many_access.xml",
            #model_a_many_2_many model_b_many_2_many
                "security/model_a_many_2_many_access.xml",
                "security/model_b_many_2_many_access.xml",
            #model_crud_inheritance
                "security/model_crud_inheritance_access.xml",
            #model_prototype_inheritance
                "security/model_prototype_inheritance_access.xml",
                "security/model_prototype_inheritance1_access.xml",
                "security/model_prototype_inheritance2_access.xml",
            #model_delegation_inheritance
                "security/model_delegation_inheritance1_access.xml",
                "security/model_delegation_inheritance2_access.xml",
                
            "security/ir.model.access.csv",
        #views
            #first_test_model
                "views/first_test_model_views.xml",
                "views/first_test_model_menus.xml",
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
            #model_crud_inheritance
                "views/model_crud_inheritance_views.xml",
                "views/model_crud_inheritance_menus.xml",
            #model_prototype_inheritance
                "views/model_prototype_inheritance_views.xml",
                "views/model_prototype_inheritance_menus.xml",
                "views/model_prototype_inheritance1_views.xml",
                "views/model_prototype_inheritance1_menus.xml",
                "views/model_prototype_inheritance2_views.xml",
                "views/model_prototype_inheritance2_menus.xml",
            #model_delegation_inheritance
                "views/model_delegation_inheritance1_views.xml",
                "views/model_delegation_inheritance1_menus.xml",
                "views/model_delegation_inheritance2_views.xml",
                "views/model_delegation_inheritance2_menus.xml",

    ],
    "demo":[
        "demo/demo.xml",
    ]

}