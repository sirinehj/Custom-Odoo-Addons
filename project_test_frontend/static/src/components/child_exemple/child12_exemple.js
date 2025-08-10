import { Component, useState } from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";
import {rpc} from "@web/core/network/rpc"
export class Child12_Exemple extends Component{
    static template="project_test_frontend.Child12_Exemple";

    //we will work with crm moduel of odoo
    //dont forget to add it in the _manifest_.py depends:[]
    //need setup()
     setup(){
        //here we will make a var for orm and use the service of it
        this.orm=useService("orm");
        //i will make a button that will create new instance in crm from our template
        //i will create numbers for crm instances
        this.counter=0;
    }
    //now in this fnc we will create the crm instance and alert for notification
    crm_create(){
        //to make the orm use any public methode you need to pass it throw call()
        //this.orm.call("model","method",data)
        //for this exemple its call("crm.lead","create",[{"name" :"i m new from child12 of testing_02 model"}])
        this.counter++;
        this.orm.call("crm.lead","create",[{"name" :String("new"+(this.counter))}]);
        alert(String("a new Num "+(this.counter)+" from child12 of testing_02 model in crm moduel go see it"));
    }
    patch_me(){
        let msg="i m patch_me original msg from child12";
        alert(msg);
        
    }
}