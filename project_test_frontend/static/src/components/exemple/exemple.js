//we are in odoo18 we dont need @odoo-module in the beginning of the file 
//first thing here is to import {Component} from '@odoo/owl';
//class name is Exemple like in exemple.xml
/*
this was from odoo video owl
import { Component } from '@odoo/owl';
import { registry } from "@web/core/registry";
export class Exemple extends Component{

    //templete=t-name value in the exemple.xml in t tag 
    static template="project_test_frontend.Exemple"
    //now we need to go to the _manifest_.py
    //and add the files exemple in assets
}
//here at the end of this class/js file im not sure about it for now
//we will converte our template in exemple.xml to a component
//in the top dont forget to import the registry
//import { registry } from "@web/core/registry";
registry.category("view_widgets").add("project_test_frontend.Exemple",{ Component:Exemple});
*/

import { registry } from "@web/core/registry";
import { Component } from '@odoo/owl';

export class Exemple extends Component {
    //template=t-name value in the exemple.xml in t tag 
    static template = "project_test_frontend.Exemple";
    //now we need to go to the _manifest_.py
    //and add the files exemple in assets
}
registry.category("view_widgets").add("project_test_frontend.Exemple",{ component:Exemple});


//and this from copilot
/*odoo.define('project_test_frontend.components.exemple', ['owl.Component'], function (require) {
    'use strict';
    const { Component } = require('@odoo/owl');
    //const { registry } = require('@web/core/registry');

    class Exemple extends Component {
        static template = 'project_test_frontend.Exemple';
    }
    
   
    return [Exemple];
});
registry.category("view_widgets").add("project_test_frontend.Exemple", { Component: Exemple });
*/

