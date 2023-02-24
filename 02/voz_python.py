from gtts import gTTS
from playsound import playsound

contador = int()
while True:
	frase = input('Digite uma frase: ')
	if frase == 'desligar':
		break
	tts = gTTS(frase, lang='pt-br', slow=False)
	tts.save(str(contador) +'-'+ 'hello.mp3')
	contador +=1

	print("Estou aprendendo o que voce disse...")
	playsound(str(contador) +'-'+ 'hello.mp3')