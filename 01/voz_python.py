from gtts import gTTS
from playsound import playsound

frase = "Ola, vamos sintetizar voz com python"
tts = gTTS(frase, lang='pt-br',slow=False)
tts.save('hello.mp3')
print("Estou aprendendo o que voce disse...")
playsound('hello.mp3')
