import { Component } from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";

export class Child10_Exemple extends Component{
    static template="project_test_frontend.Child10_Exemple";
    //this child10.js will use the my_exemple_service.js
    // it only need setup()
    setup(){
            //here i will use the service using useService()
            //it need to be imported from "@web/core/utils/hooks"
            //then my service in this case => userService("child10_service");
            //then i will alert the value and it need to be the value of msg from the my_exemple_service.js
            useService("child10_service");
            alert("useService('child10_service') value is: "+useService("child10_service"));
        
    }
}