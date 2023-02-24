import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice','brazil')

while True:
	frase = str(input('Digite um texto: '))
	if frase == '0':
		break

	engine.say(frase)
	engine.runAndWait()