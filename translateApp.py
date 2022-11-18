import speech_recognition as sr
from googletrans import Translator

def traduzir_fala(lingua_traduzir,lingua_traduzida):
    print(Translator().translate('Wait', dest = lingua_traduzida).text + ' ...')

    microfone = sr.Recognizer() #Habilita o microfone
    with sr.Microphone() as source:        
        microfone.adjust_for_ambient_noise(source)#Reducao de ruido disponivel na speech_recognition        
        print(Translator().translate('Say something', dest = lingua_traduzida).text+ ': ')
        audio = microfone.listen(source) #guarda o audio falado na variavel 'audio', o audio é finalizado nas pausas grandes
        try:
            frase = microfone.recognize_google(audio, language = lingua_traduzir)
            frase_trans = Translator().translate(frase, dest = lingua_traduzida).text

            print(Translator().translate('You said', dest = lingua_traduzida).text + ': ' + frase_trans)    
        except:
            print(Translator().translate('Sorry, I could not understand', dest = lingua_traduzida).text)
        return frase

traduzir_fala('fr', 'pt')