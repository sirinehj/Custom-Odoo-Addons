import { Component } from "@odoo/owl";;

export class Child3_Exemple extends Component{
    static template = "project_test_frontend.Child3_Exemple";
    static props={
        title:{type:String},
        //adding the slots
        slots:{type:Object},
    }


}