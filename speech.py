# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
 
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
 
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
	x = r.recognize_google(audio)
	if x == 'question mark':
		x = '?'
	elif x == 'plus':
		x = '+'
	
	print("You said: " + x)
	with open("speech.txt","w") as f:
		f.write(x)
		f.close()
	
except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
