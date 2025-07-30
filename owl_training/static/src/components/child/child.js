import { Component, onWillStart, useRef } from "@odoo/owl";

export class Child extends Component {
    static template = "owl_training.Child";
    static props = {
        title: { type: String},
        list: { type : Array},
        slots: { type: Object },
        counter: { type: Number},
    };


    setup(){
        this.myInputRef = useRef("my-input");
        onWillStart(() => console.log("Child onWillStart"));
    }

    focusMyInput(){
        this.myInputRef.el.focus();
    }


}

