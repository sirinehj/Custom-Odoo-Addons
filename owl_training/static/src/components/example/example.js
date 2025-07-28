/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class Example extends Component {
    static template = "owl_training.Example";
}

registry.category("view_widgets").add("example", {
    component: Example
});