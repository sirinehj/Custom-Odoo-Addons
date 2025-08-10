import {registry} from "@web/core/registry";

registry.category("services").add("child11_weather_service",{
    start(){
    //start(){
        //console.log("child11_weather_service");
        //alert("child11_weather_service");
        //in this service i will just return the API
        let api="https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m";
        return api;
        //now i will go to child11.js
    }
});