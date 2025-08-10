import { Component} from "@odoo/owl";

export class Child4_Exemple extends Component{
    static template = "project_test_frontend.Child4_Exemple";
    static props = {
        title:{type:String},
        slots:{type:Object},
    }

}