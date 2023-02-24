from gtts import gTTS
from playsound import playsound

f = open('frase.txt','r',encoding='utf-8')
conteudo = f.read()
print(conteudo)

frase=conteudo
tts = gTTS(frase, lang='pt-br',slow=False)
tts.save('hello.mp3')
print("Estou aprendendo o que voce disse...")
playsound('hello.mp3')
f.close()