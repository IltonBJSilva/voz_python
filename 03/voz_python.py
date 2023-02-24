from time import sleep

from gtts import gTTS
from playsound import playsound

while True:
	frase = input('Digite uma frase: ')
	if frase == 'desligar':
		break
	nome_arq = input('Digite o nome do arquivo + .mp3: ')
	tts = gTTS(frase, lang='pt-br', slow=False)
	tts.save(nome_arq)
	sleep(2)

	print("Estou aprendendo o que voce disse...")
	playsound(nome_arq)