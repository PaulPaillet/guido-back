import speech_recognition as sr
import array
import os

def functionPourTEst(input):
    input.test = "ich ich"
    return input

def translate(input):
    return (256+input)%256

def testFileTObite():
    byte_array = array.array('B')
    audio_file = open('notes.flac', 'rb')
    byte_array.fromstring(audio_file.read())
    audio_file.close()
    r = sr.Recognizer()
    data = sr.AudioData(byte_array, 11025 , 4)
    result = r.recognize_google(data, language="fr-FR")
    return result

def testFile():
    byte_array = array.array('B')
    audio_file = open('notes.flac', 'rb')
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
    tmp = []
    for i in range(0, len(body.value)):
        tmp.append(translate(body.value[i]))
    byte_array = array.array('B')
    byte_array.fromlist(tmp)
    f = open('reg.3gp', 'wb')
    f.write(byte_array)
    f.close()
    filename = 'reg.wav'
    os.system('ffmpeg -i reg.3gp reg.wav')
    r = sr.Recognizer()
    data = "null"
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
        try:
            data = r.recognize_google(audio, language="fr-FR")
            print(data)
        except:
            print("Please try again")
    return data
