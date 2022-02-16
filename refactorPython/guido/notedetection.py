import speech_recognition as sr
import array
import os
from os.path import curdir, join as pjoin
from charset_normalizer import detect
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt


def functionPourTEst(input):
    input.test = "ich ich"
    return input

def translate(input):
    return (256+input)%256

def testFileTObite():
    byte_array = array.array('B')
    audio_file = open('notes_test.flac', 'rb')
    byte_array.fromstring(audio_file.read())
    audio_file.close()
    r = sr.Recognizer()
    data = sr.AudioData(byte_array, 11025 , 4)
    result = r.recognize_google(data, language="fr-FR")
    return result

def testFile():
    byte_array = array.array('B')
    audio_file = open('notes_test.flac', 'rb')
    byte_array.fromstring(audio_file.read())
    #audio_file.close()
    r = sr.Recognizer()
    filename = 'ttt.wav'
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
        try:
            data = r.recognize_google(audio, language="fr-FR")
            print(data)
        except:
            print("Please try again")
    #data = sr.AudioData(byte_array, 32532, 1)
    #result = r.recognize_google(data, language="fr-FR")
    return "oui"


def processNote(body):
    print(body.sampleRate, body.sampleWidth)
    tmp = []
    for i in range(0,len(body.value)):
        tmp.append(translate(body.value[i]))
    byte_array = array.array('B')
    byte_array.fromlist(tmp)
    r = sr.Recognizer()
    data = sr.AudioData(byte_array, body.sampleRate, body.sampleWidth)
    result = r.recognize_google(data, language="fr-FR")
    print(result)
    return result

def processNoteByFile(body):
    # Get bytes array from the app
    # The app register sound as .3gp
    # Then send it as a bytes array
    tmp = []
    for i in range(0, len(body.value)):
        tmp.append(translate(body.value[i]))
    byte_array = array.array('B')
    byte_array.fromlist(tmp)

    # Store bytes array in a file to recognize and convert it
    with open('reg.3gp', 'wb') as f:
        f.write(byte_array)

    # Convert .3gp to .wav
    filename = 'reg.wav'
    if os.path.exists(filename):
        os.remove(filename)
    os.system('ffmpeg -i reg.3gp reg.wav')

    sonenvoye = pjoin(curdir, filename)
    samplerate, datate = wavfile.read(sonenvoye)

    #print(f"number of channels = {datate.shape[1]}")
    length = datate.shape[0] / samplerate
    print(f"length = {length}s")
    print(datate.shape[0])

    
    time = np.linspace(0., length, datate.shape[0])
    #plt.plot(time, datate, label="Left channel")
    #plt.legend()
    #plt.xlabel("Time [s]")
    #plt.ylabel("Amplitude")
    #plt.show()

    ##########
    # Deleting blanc noise

    c = 0
    # 1000-1050 : [0 1]
    l = []
    seuil = 0
    son = 1
    tab = []

    detectNote = False
    for d in datate:
        if abs(d) > 2000:
            detectNote = True
            l.append(d)
        elif seuil < 3000 and detectNote:
            print(seuil)
            l.append(d)
            seuil +=1
        else:
            if detectNote:
                tab.append(l)
                l = []
            detectNote = False
            seuil = 0
    print("---")
    print(len(tab))
    print("---")

    longueurNoteTab = ""

    for t in tab:
        data_bis = np.array(np.array(t))
        wavfile.write(str(son) + ".wav", samplerate, data_bis.astype(np.int16))
        wav_fname1 = pjoin(curdir, str(son) +'.wav')
        samplerate1, data1 = wavfile.read(wav_fname1)
        #print(f"number of channels = {data.shape[1]}")

        length1 = data1.shape[0] / samplerate1

        longueurNoteTab += str(length1) + " "

        #print(f"length = {length}s")
        #print(data.shape[0])
        time = np.linspace(0., length1, datate.shape[0])
        print("Le son " +str(son) + " dure " + str(round(length1,2))+"s")
        son +=1

    for long in longueurNoteTab:
        print(long)


    # Start recognition
    r = sr.Recognizer()
    data = "null"

    with sr.AudioFile(filename) as source:
        audio = r.record(source)
        try:
            data = r.recognize_google(audio, language="fr-FR")
            print(data)
        except:
            print("Please try again")
    return data + " " + longueurNoteTab
