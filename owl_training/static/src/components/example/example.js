import { Component, useState, useSubEnv } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { Child } from "../child/child"; 
import { useService } from "@web/core/utils/hooks";

export class Example extends Component {
    static template = "owl_training.Example";
    static components = { Child };

    setup(){
        useSubEnv({data : "info"});
        //this.myService = useService("my-service");
        this.orm = useService("orm");
        this.state = useState({counter: 0});
        this.message="Hello!";
    }

    increment(event){
        this.state.counter++;
        this.orm.call("crm.lead", "create", [{ "name": "new"}]);
    }


    alertMessage(event){
        alert(this.message);
    }

}

registry.category("view_widgets").add("example", {
    component: Example
});