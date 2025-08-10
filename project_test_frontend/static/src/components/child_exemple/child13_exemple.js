import { Component, useState } from "@odoo/owl";
import {patch} from "@web/core/utils/patch";
import { Child12_Exemple } from "./child12_exemple";

export class Child13_Exemple extends Component{
    static template="project_test_frontend.Child13_Exemple";

    
    //let's store the original patch_me()
    static patch_me_originale=Child12_Exemple.prototype.patch_me;
    patching(){
        //need to import patch() from "@web/core/utils/patch"
        //patch(class.prototype,your logic of the override method)
        patch(Child12_Exemple.prototype,{
            patch_me(){
                this.msg="this msg is overided by child13";
                
            }
        });
    }
    //well it dosen't work but no err to fix ...
    
}