import { Component } from "@odoo/owl";

export class Child1_Exemple extends Component{
    static template="project_test_frontend.Child1_Exemple";
    // after setting the basic of child1_exemple.js and child1_exemple.xml
    // we will go to the parent component exemple.xml to link the child1 component
    //now we will add a prop to this component
    //so it will be like static props = { prop1: { type: String }, prop2: { type: Number },... };
    static props = {
        title:{type:String}
    };
    //now we will go to the exemple.js to add the child component
}

    