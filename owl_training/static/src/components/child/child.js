import { Component, onWillStart, onWillDestroy } from "@odoo/owl";

export class Child extends Component {
    static template = "owl_training.Child";
    static props = {
        title: { type: String},
        list: { type : Array},
        slots: { type: Object },
    };


    setup(){
        onWillStart(() => console.log("Child onWillStart"));
        onWillDestroy(() => alert("Destroying"));
    }
}

