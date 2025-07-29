{
    "name":"testing_02",
    "summary":"Testing owl odoo",
    "license":"LGPL-3",
    "version":"1.0",
    "depends":[],
    "data":[
        #security
                #fronting access
                "security/fronting_access.xml",



            "security/ir.model.access.csv",
        #views
            #fronting model
                "views/fronting_testing_02_views.xml",
                "views/fronting_testing_02_menus.xml",
                #inherited views
                   "views/project_test_frontend_fronting_testing_02_views.xml",
                
            
    ],
    "demo":[],
   "assets":{
        #assets is a dict of arrays
        #assets keys are :
        # web.assets_common: this bundle is for the web client, the website and also the point of sale. 
        #   This is supposed to contain lower level building blocks for the odoo framework. Note that 
        #   it contains the boot.js file, which defines the odoo module system.
        #web.assets_backend: this bundle is for the code specific to the web client 
        #   (notably the web client/action manager/views/static XML templates)
        #web.assets_frontend: this bundle is for all that is specific to the public website: ecommerce, 
        #   portal, forum, blog, …
        #web.qunit_suite_tests: all javascript qunit testing code (tests, helpers, mocks)
        #web.qunit_mobile_suite_tests: mobile specific qunit testing code
        "web.assets_backend":[
            #and here we add the static xml js files
            #for now we will add all
            #we need the technical name of the model in odoo apps we can see it in the developer mode
            "project_test_frontend/static/src/components/**/*",
            #if you had a security err in server so i will add it file by file
            #"project_test_frontend/static/src/components/exemple/exemple.js",
            #"project_test_frontend/static/src/components/exemple/exemple.xml",
            #to have more controle on everyfile we can put in 
            #('before',"static/src/componets/..."),
            #the parameters before the path are:
            # append: path
            #prepend: path
            #before: target, path
            #after: target, path
            #include: path (interpreted as a bundle name)
            #remove: path (interpreted as a target asset to remove)
            #replace: target, path
        #add to your commande --dev=all
        #after that we go to 127.0.0.1/8069 install the model in odoo then enable dev mode with assets
        #then press F12 and go to source tab you will find an orange folder check if your static is inside
        #so if you have your model their that's mean you are load your assets in odoo bundles
        ]
    }
   
}