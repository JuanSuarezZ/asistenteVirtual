import turtle
import time 
import random

posponer = 0.1

#Configuracion de la ventana
wn = turtle.Screen()
wn.title('juego de snake')
wn.bgcolor('black')
wn.setup(600, 600)
wn.tracer()

#cabeza de serpiente

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'
cabeza.color('white')


#comida

comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup()
comida.goto(0,100)
comida.color('red')

#Segmentos / cuerpo serpiente

segmentos = []

#Funciones

def arriba():
    cabeza.direction = 'up'

def abajo():
    cabeza.direction = 'down'

def izquierda():
    cabeza.direction = 'left'

def derecha():
    cabeza.direction = 'right'




def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
#teclado

wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')



while True:
    wn.update()
    #colision comida 
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.penup()
        nuevo_segmento.color('grey')
        segmentos.append(nuevo_segmento)

    # Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()
    time.sleep(posponer)