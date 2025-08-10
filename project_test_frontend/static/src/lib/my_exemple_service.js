import { registry}  from "@web/core/registry";

registry.category("services").add("child10_service",{

    //in this service i will just alert and notify the user when the
    //child10 is load in the DOM
    dependencies:["notification"],
    start(env,{notification}){
    //start(){   
        console.log("child10_service"); 
        let msg="hi from Child 10 using my a service\n im load and ready thanks to child10_service from my_exemple_service.js";
        alert("Alerting: "+msg);
        notification.add(msg);
        return msg;
    }
});