import pyaudio
import wave
import speech_recognition as sr
r = sr.Recognizer()
filename = "sound/do1.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio = r.record(source)
    try:
        data = r.recognize_google(audio, language="fr-FR")
        print(data)
    except:
        print("Please try again")