import pyttsx3

speaker = pyttsx3.init()
speaker.setProperty("rate",100)
speak = input("Enter words to say :")
speaker.say(speak)
speaker.runAndWait()