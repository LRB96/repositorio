import turtle

#Ventana
screen = turtle.Screen()
screen.title("Pong-Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


#JugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5, stretch_len=1)

#JugadorB
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1)

#Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.goto(0,0)
pelota.penup()
# pelota.shapesize(stretch_wid=1, stretch_len=1)
pelota.dx = 1
pelota.dy = 1

#Division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#Funciones para el movimiento de jugadores

                    #Movimiento jugadorA
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

                   #Movimiento jugadorB
def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

#Teclado
screen.listen()

#Movimiento de JugadorA
screen.onkeypress(jugadorA_up, "w")
screen.onkeypress(jugadorA_down, "s")

#Movimiento de JugadorB
screen.onkeypress(jugadorB_up, "Up")
screen.onkeypress(jugadorB_down, "Down")


while True:
    screen.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #Bordes arriba/abajo
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1
    
    #Bordes derecha/izquierda
    if pelota.xcor() > 390 or pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1