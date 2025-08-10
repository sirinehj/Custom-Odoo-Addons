import { Component } from "@odoo/owl";

export class Child2_Exemple extends Component{
    static template="project_test_frontend.Child2_Exemple";
    // after setting the basic of child2_exemple.js and child2_exemple.xml
    // we will go to the parent component exemple.xml to link the child2 component
    //now we will add a prop to this component
    //so it will be like static props = { prop1: { type: String }, prop2: { type: Number },... };
    static props = {
        title:{type:String},
        //here we will add the prop list and ofc it will be an array
       // list:{type:Array},
        //now we will go to the exemple.xml in the Child_Exemple component tag
        //to add the new prop
        list:{type:Array},
    };
    //now we will go to the exemple.js to add the child component
    //now we will create a function that will be use the this.var and we will call the var in the template
    //child2_exemple.xml
    // it need to be called in function setup
    // setup() in owl is where you initialize your component’s state, props, 
    // and any reactive data or logic
    setup(){
        // i will say something="Hello from Child2_Exemple component";
        // thats why i will add this.something = "Hello from Child2_Exemple component"
        this.something = "Hello from Child2_Exemple component";
        //now we go back to the child2_exemple.xml and add a p tag like
        //<p> counter:<t t-out="something"/></p>
    }
}

    