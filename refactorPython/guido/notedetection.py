import speech_recognition as sr
import array

import models


def functionPourTEst(input):
    input.test = "ich ich"
    return input


def processNote(body):
    tmp = []
    for i in range(0,len(body.value)):
        tmp.append(body.value[i]+128)
    byte_array = array.array('B')
    byte_array.fromlist(tmp)
    print(byte_array)
    with open('oui.flac', mode='wb') as f:
        f.write(byte_array)
    #r = sr.Recognizer()
    #data = sr.AudioData(byte_array, body.sampleRate, body.sampleWidth)
    #result = r.recognize_google(data, language="fr-FR")
    return "do"
