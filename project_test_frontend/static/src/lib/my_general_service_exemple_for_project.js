//here first things first we need to know that a service in odoo/owl
//is regestry that use a start() and most of imports are from "@web" not "owl"
// the syntax will be like 
/*
import { registry}  from "@web/core/registry";

//adding my-service to odoo services
registry.category("services").add("my-service",{
    //we can use dependencies (its services here not moduels) just like in _manifest_.py
    //here the doc :https://docs.advanceinsight.dev/developer/reference/frontend/services.html
    //in the satrt() it take the envirement and services of dependenies
    dependencies:["notification"],
    start(env,{notification}){
        //logic with notification instance
        return //logic;
    }
});
*/
import { registry}  from "@web/core/registry";

registry.category("services").add("my-general_service_testing_02",{
        //here after logining to odoo i will alert welcome msg and use
        //notification service to make welcome msg in notification
        // and return welcome var as true
        dependencies:["notification"],
        start(env,{notification}){
        //if something happen (like err with import ...) try to debug by conseling step by step
        //and that will fix all till you can run everything
        //start(){ 
        //    console.log(" service of my-general_service_testing_02");
        let welcomed=null;  
        alert("Welcome to odoo from my-general_service_testing_02");
          notification.add("Welcome to odoo from my-general_service_testing_02 using notification service of odoo");
          return welcomed=true;  
        }
});
