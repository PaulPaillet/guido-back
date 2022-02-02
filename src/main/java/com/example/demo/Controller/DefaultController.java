package com.example.demo.Controller;


import com.example.demo.Model.Body;
import com.example.demo.Model.Dto;
import com.example.demo.Service.SoundService;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.web.bind.annotation.*;

import java.nio.file.LinkPermission;

@RestController
public class DefaultController {

    SoundService soundService = new SoundService();

    @GetMapping("/test")
    public String testRoute(){
        ObjectMapper obj = new ObjectMapper();
        String str="as de valeur";
        try{
            str = obj.writeValueAsString(soundService.testDTo());
        }catch (Exception e){
            e.printStackTrace();
        }
        return str;
    }


    @PostMapping("/process")
    public Dto processAudio(@RequestBody Body input){

        return soundService.processAudio(input);
    }


}
