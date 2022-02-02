import pyaudio
import wave
import speech_recognition as sr
import array
import wave
import sys

filename = "D:/polytech/SI5/elimp/projet/ELIMP/elimpBackend/src/main/resources/sound/do1.wav"

if __name__ == "__main__":
	#Quand on aura tout la chaine on rempalacera par sys.argv[x] pour passer en paramêtre
	byte_array = array.array('B')
	audio_file = open(sys.argv[1], 'rb')
	byte_array.fromstring(audio_file.read())
	#print(len(byte_array))


	audio_file.close()
	r = sr.Recognizer()
	data = sr.AudioData(byte_array,int(sys.argv[2]),int(sys.argv[3]))
	result = r.recognize_google(data,language="fr-FR")
	print(result)
