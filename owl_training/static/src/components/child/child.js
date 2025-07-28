import { Component } from "@odoo/owl";

export class Child extends Component {
    static template = "owl_training.Child";
    static props = {
        title: { type: String},
        list: { type : Array},
    };
}

