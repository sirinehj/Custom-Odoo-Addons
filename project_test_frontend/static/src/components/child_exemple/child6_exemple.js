import {Component,onWillStart,onWillDestroy} from "@odoo/owl";
export class Child6_Exemple extends Component{
 static template="project_test_frontend.Child6_Exemple";

    //on the setup() we will use the lifecycle
    setup(){
        //onWillStart() =>	async, before first rendering
        //onWillRender() =>	just before component is rendered
        //onRendered()	=> just after component is rendered
        //onMounted() =>	just after component is rendered and added to the DOM
        //onWillUpdateProps()	=> async, before props update
        //onWillPatch() =>	just before the DOM is patched
        //onPatched() =>	just after the DOM is patched
        //onWillUnmount() =>	just before removing component from DOM
        //onWillDestroy() =>	just before component is destroyed
        //onError() =>	catch and handle errors (see error handling page)
        //all of them need to be imported from "@odoo/owl"
        onWillStart(()=>{
            alert("child6 is starting now");
        });
        onWillDestroy(()=>{
            alert("child6 is destroying now");
        });
    }
}