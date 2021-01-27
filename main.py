import webbrowser
import threading
import time
import os
import speech_recognition as sr

r = sr.Recognizer()
x = True
rutas = {'google' : 'https://google.com', 
         'facebook' : 'https://www.facebook.com',
        }

print('Bienvenido, sere tu asistente por voz :) ')

def escuchar():
    
    with sr.Microphone() as source:
        
        print("entro al hilo")
        audio = r.listen(source)
       
        try:
            text = r.recognize_google(audio,language="es-ES")
            print('has dicho: {}'.format(text))

            txt = text.lower()
            opciones = txt.split()
            opciones2 = txt.split("buscar")
            opciones3  = txt.split("guarda esto")

            print(opciones2)


            if opciones[0] == 'abrir':
                webbrowser.open( rutas[opciones[1]] )
                thread._stop 

            if opciones[0] == 'agregar':
                rutas[ opciones[1] ] = opciones[2]
                thread._stop
            
            if opciones[0] == 'buscar':
                busqueda = 'https://www.google.com/search?q='+ opciones2[1]
                webbrowser.open( busqueda )
                thread._stop
            
            if opciones[0] == 'guarda' and opciones[1] == 'esto':
                
                file = open("C:\holamundo.txt","w")
                file.write("hola mundo\n")
                file.close()

                print("va a guardar: ",opciones3[1])
                thread._stop

            if opciones[0] == 'jugar' and opciones[1] == 'culebrita': 
                os.system('python culebrita.py')
                thread._stop 

            

        except:
            print("No he podido entenderte")
         


while x == True:

    with sr.Microphone() as source:

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio,language="es-ES")
            print('has dicho: {}'.format(text))
            opciones = text.lower().split()

            if opciones[0] == 'comando':
            
                thread = threading.Thread(target=escuchar)
                thread.start()
                thread.join()
            
            if opciones[0] == 'salir':
                x = False
         
                
       
        except:
            print("intenta de nuevo")











