import { Component,onMounted } from "@odoo/owl";
export class Child5_Exemple extends Component {
    static template = "project_test_frontend.Child5_Exemple";

    //first in the setup() we will define the message to alert
    setup() {
        this.message = "Child 5 Exemple Button Clicked";
        
    }
    //here i will add the button click event with t-on-click t-on-[event]
    Clickme() {
        //now we will alert the message
        //this.message is the message defined in the setup()
        alert(this.message);
    }
   
}
