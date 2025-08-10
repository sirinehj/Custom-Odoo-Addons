import { Component } from "@odoo/owl";
import {useService} from "@web/core/utils/hooks";
import {rpc} from "@web/core/network/rpc"
export class Child11_Exemple extends Component{
    static template="project_test_frontend.Child11_Exemple";

    //need to get the api from my service
    //i need to use rpc
     setup(){
        //useService("child11_weather_service");
        //now to get the response i need rpc
        //import rpc from "@web/core/network/rpc"
        //rpc(url)
        //but rpc() is used for backend odoo using json-rpc
        //so the only way is with fetch
        /*async ()=>{
            alert(useService("child11_weather_service"));
           const response= await fetch(useService("child11_weather_service"));
            response.json().then((res)=>{
                console.log("api res:",res);
                alert("api res:"+res);
            }).catch((err)=>{
                console.log("err",err);
                alert("api err:"+err);
            });
        }*/
       //well if fetch dont want to work i will use ajax old but gold
       console.log("child11 service:",useService("child11_weather_service"));
       let url=useService("child11_weather_service");
       let xhr= new XMLHttpRequest;
       xhr.open("GET",url);
       xhr.send();
       xhr.onload=()=>{
            //converting response to json => JSON.parse(response)
            if(xhr.responseText){
                let data=JSON.parse(xhr.responseText);
                console.log("weather data",data);
                let p = document.getElementById("data_p");
                if((xhr.responseText)!=null)
                {
                    p.innerHTML=xhr.responseText;
                }
            }
        }
       //well for me ajax is better then fetch
        
    }
}