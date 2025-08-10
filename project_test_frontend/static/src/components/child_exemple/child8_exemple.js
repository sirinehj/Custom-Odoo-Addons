import { Component, useRef } from "@odoo/owl";

export class Child8_Exemple extends Component{
    static template="project_test_frontend.Child8_Exemple";
    //no need for props no need to be controlled by exemple
    //need setup()
    //need focusing_input()
    setup(){
        //we need to def var to use useRef()
        //import useRef from"@odoo/owl"
        this.input=useRef("input_ref");
        //now we go to focusing_input()

    } 
    focusing_input(){
        //el is a proprety in owl to access to dom elements
        //we can use focus() bc of el
        this.input.el.focus();
        alert("you clicked on 'focus input' to focus me");
    }
}