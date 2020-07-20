import pyttsx3

data = input("Enter text")
engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()
