import pyttsx3
from comandos import comandoAtivacao, comandoRespostaBem, comandoRespostaMal,comandoAgradecimento
from random import choice

engine = pyttsx3.init()
velocidadeFala = engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
for voice in voices:
	engine.setProperty('voice', voice.id)



def reconhece():
	from datetime import datetime
	import pywhatkit
	import speech_recognition as sr
	from random import randint
	mic = sr.Recognizer()
	with sr.Microphone() as fala:
		mic.adjust_for_ambient_noise(fala)
		while True:
			try:
				audio = mic.listen(fala)
				entrada = mic.recognize_google(audio,language='pt-BR')
				print(f'você disse: {entrada}')
				entrada = entrada.lower()

				if entrada == 'oi elison' or entrada =='ei elison' or entrada == 'olá elison':
					resp =choice(comandoAtivacao)
					print(resp)
					reproduz(resp)

				elif entrada == 'eu estou bem' or entrada == 'bem graças a deus' or entrada == 'tudo ótimo' or entrada == 'bom' or entrada == 'estou bem':
					resp=choice(comandoRespostaBem)
					print(resp)
					reproduz(resp)

				elif entrada == 'não estou bem' or entrada == 'nada bem' or entrada == 'estou estressado':
					resp = choice(comandoRespostaMal)
					print(resp)
					reproduz(resp)

				elif 'quantas horas' == entrada or 'horário de agora' == entrada or entrada == 'quantas horas são':
					agora = datetime.now()
					hora = (f'São {agora.hour}horas e {agora.minute}minutos')
					reproduz(hora)

				elif entrada == 'obrigado' or entrada == 'muito obrigado':
					resp = choice(comandoAgradecimento)
					print(resp)
					reproduz(resp)

				elif 'pesquisar no google' in entrada:
					termo = entrada.split('pesquisar no google')
					pesquisa = termo[1]
					print(pesquisa)
					pywhatkit.search(pesquisa)
					reproduz(f'pesquisando por {pesquisa}')	

				elif 'pesquisar no youtube' in entrada:
					termo = entrada.split('pesquisar no youtube')
					pesquisa = termo[1]
					print(pesquisa)
					pywhatkit.playonyt(pesquisa)
					reproduz(f'pesquisando por {pesquisa}')	

				elif entrada == 'desligar':
					tempo = 10 
					reproduz('tchau, espero ter ajudado')
					pywhatkit.shutdown(tempo)

				elif entrada == 'cancelar': 
					reproduz('ok, não vou desligar')
					pywhatkit.cancelShutdown()
					
			except sr.UnknownValueError:
				return ''
			
			
def reproduz(frase):
	engine.say(frase)
	return engine.runAndWait()


def Allison():
	while True: 		
		Allison = reconhece()
		return reproduz(Allison)
	

assistente = Allison()
