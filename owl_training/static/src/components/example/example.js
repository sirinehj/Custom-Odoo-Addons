import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { Child } from "../child/child"; 

export class Example extends Component {
    static template = "owl_training.Example";
    static components = { Child };

}

registry.category("view_widgets").add("example", {
    component: Example
});