package com.example.demo.Service;


import com.example.demo.Model.Body;
import com.example.demo.Model.Dto;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class SoundService {

    public static final String PATH_TO_SCRIPT = "D:\\polytech\\SI5\\elimp\\projet\\ELIMP\\elimpBackend\\src\\main\\resources\\pythonScript.py";
    public static  final  String PATH_TO_AUDIO_TEST = "D:/polytech/SI5/elimp/projet/ELIMP/elimpBackend/src/main/resources/sound/do1.wav";
    public SoundService(){

    }



    public Dto processAudio(Body body)  {
        String str = "";
        try{
            String command = "cmd /c python "+PATH_TO_SCRIPT + " "+  PATH_TO_AUDIO_TEST + " "+ body.sampleRate + " " + body.sampleWidth;
            Process p = Runtime.getRuntime().exec(command);
            p.waitFor();
            BufferedReader bri = new BufferedReader(new InputStreamReader(p.getInputStream()));
            BufferedReader bre = new BufferedReader(new InputStreamReader(p.getErrorStream()));
            String line;
            while ((line = bri.readLine()) != null) {
                System.out.println(line);
                str+=line;
            }
            bri.close();
            while ((line = bre.readLine()) != null) {
                System.out.println(line);
            }
            bre.close();
            p.waitFor();
            System.out.println("Done.");

            p.destroy();
        }catch (Exception e){

        }
        Dto res = new Dto();
        res.note = str;
        return res;
    }

    public Dto testDTo(){
        Dto rep = new Dto();
        rep.note = "do";
        return  rep;
    }

    public String test() {
        String str = "";
        try{
            String command = "cmd /c python "+PATH_TO_SCRIPT;
        Process p = Runtime.getRuntime().exec(command);
        p.waitFor();
        BufferedReader bri = new BufferedReader(new InputStreamReader(p.getInputStream()));
        BufferedReader bre = new BufferedReader(new InputStreamReader(p.getErrorStream()));
        String line;
        while ((line = bri.readLine()) != null) {
            System.out.println(line);
            str+=line;
        }
        bri.close();
        while ((line = bre.readLine()) != null) {
            System.out.println(line);
        }
        bre.close();
        p.waitFor();
        System.out.println("Done.");

        p.destroy();
        }catch (Exception e){

        }
        return str;
    }



}
