import webbrowser
import speech_recognition as sr

r = sr.Recognizer()


while True:

    with sr.Microphone() as source:
        print('Bienvenido, sere tu asistente por voz: ')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('has dicho: {}'.format(text))
            print(text)
            if 'Google' or 'google' in text:
                webbrowser.open('https://google.com')
            if "Facebook" or 'facebook' in text:
                webbrowser.open('https://www.facebook.com')

        except:
            print("no he entendido")








