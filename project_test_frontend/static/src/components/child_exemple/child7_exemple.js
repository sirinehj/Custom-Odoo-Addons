import { Component } from "@odoo/owl";

export class Child7_Exemple extends Component{
    static template="project_test_frontend.Child7_Exemple";
    //here i will set the state counter as props
    static props={
        counter:{type:Number},
    }
    //good now we go to the exemple.js for using the useState func and get control of
    //counter
}