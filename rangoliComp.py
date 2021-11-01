#imports
from turtle import*
import turtle as t
#variables
screen = t.Screen()
ganesh = t.Turtle()
blue = '#10557d'
white = '#ffffff'
red = '#ff0004'
black = '#000000'
yellow = '#ffb700'

screen.title('Rangoli Drawing')

screen.bgcolor('black')
ganesh.speed(0)

ganesh.penup()
ganesh.backward(550)
ganesh.left(90)
ganesh.forward(200)
ganesh.right(90)


color('red', 'yellow')
begin_fill()
speed(0)
while True:
    backward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()


# pentagon
ganesh.color(blue, blue)
ganesh.begin_fill()
ganesh.left(angle=130)
ganesh.forward(distance=55)
ganesh.right(90)
ganesh.forward(70)
ganesh.right(65)
ganesh.forward(70)
ganesh.right(80)
ganesh.forward(55)
ganesh.right(70)
ganesh.forward(66)
ganesh.end_fill()

ganesh.penup()
ganesh.forward(10)
ganesh.left(90)
ganesh.forward(12.5)
ganesh.pendown()

#square
ganesh.color(yellow, yellow)
ganesh.begin_fill()
ganesh.forward(90)
for _ in range(3):
    ganesh.left(90)
    ganesh.forward(90)
ganesh.end_fill()

ganesh.penup()
ganesh.forward(10)
ganesh.pendown()

#rectangle 1
ganesh.color(red, red)
ganesh.begin_fill()
for _ in range(2):
    ganesh.forward(27.5)
    ganesh.right(90)
    ganesh.backward(90)
    ganesh.right(90)

ganesh.penup()
ganesh.right(180)
ganesh.forward(137.5)
ganesh.pendown()

#rectangle 2
for _ in range(2):
    ganesh.backward(27.5)
    ganesh.right(90)
    ganesh.forward(90)
    ganesh.right(90)
ganesh.end_fill()

ganesh.penup()
ganesh.left(180)
ganesh.forward(57.5)
ganesh.left(90)
ganesh.forward(5)
ganesh.left(90)
ganesh.pendown()

# Bindi line 1
ganesh.color(white)
ganesh.backward(50)

ganesh.penup()
ganesh.right(90)
ganesh.forward(5)
ganesh.left(90)
ganesh.pendown()

#Bindi line 2
ganesh.forward(50)

ganesh.penup()
ganesh.right(90)
ganesh.forward(5)
ganesh.left(90)
ganesh.pendown()

#Bindi line 3
ganesh.backward(50)

ganesh.penup()
ganesh.right(90)
ganesh.forward(10)
ganesh.pendown()

#Eye 1
ganesh.color(white, white)
ganesh.begin_fill()
ganesh.circle(5)

ganesh.penup()
ganesh.left(90)
ganesh.forward(50)
ganesh.pendown()

#Eye 2
ganesh.circle(5)
ganesh.end_fill()

ganesh.penup()
ganesh.right(180)
ganesh.forward(30)
ganesh.left(90)
ganesh.forward(25)
ganesh.pendown()

#Nose
ganesh.color(red, red)
ganesh.begin_fill()
ganesh.forward(100)
ganesh.left(90)
ganesh.forward(50)
ganesh.left(90)
ganesh.forward(20)
ganesh.left(90)
ganesh.forward(30)
ganesh.right(90)
ganesh.forward(80)
ganesh.end_fill()

# finisher
ganesh.penup()
ganesh.backward(200)
ganesh.right(90)
ganesh.forward(800)


#rangoli
l=['#FF2626','#FFF338','#FF2626','#FFF338','#FF2626','#FFF338','#FF2626','#FFF338','#FF2626','#FFF338']
ganesh.pensize(4)

ganesh.pendown()

def drawcircle(radius):
    for i in range(10):
        
        ganesh.circle(radius)
        radius=radius-4

def drawdesign():
    for i in range(10):
        ganesh.pencolor("#F50021")
        drawcircle(150)
        ganesh.right(36)
drawdesign()



#diyas
ganesh.pencolor('red')
ganesh.penup()
ganesh.right(5)
ganesh.backward(900)
ganesh.right(90)
ganesh.forward(230)
ganesh.left(90)

ganesh.pendown()
ganesh.fillcolor("#AE3509")
ganesh.begin_fill()
ganesh.left(-90)
ganesh.circle(90,180)
ganesh.left(90)
ganesh.pendown()
ganesh.forward(180)
ganesh.end_fill()
ganesh.penup()

ganesh.fillcolor("yellow")
ganesh.begin_fill()
ganesh.backward(90)
ganesh.right(45)
ganesh.pendown()
ganesh.circle(-60,90)
ganesh.right(90)
ganesh.circle(-60,90)
ganesh.end_fill()

#diya2
ganesh.penup()
ganesh.left(135)
ganesh.forward(100)

ganesh.pendown()
ganesh.fillcolor("#AE3509")
ganesh.begin_fill()
ganesh.left(-90)
ganesh.circle(90,180)
ganesh.left(90)
ganesh.pendown()
ganesh.forward(180)
ganesh.end_fill()
ganesh.penup()

ganesh.fillcolor("yellow")
ganesh.begin_fill()
ganesh.backward(90)
ganesh.right(45)
ganesh.pendown()
ganesh.circle(-60,90)
ganesh.right(90)
ganesh.circle(-60,90)
ganesh.end_fill()

#diya3
ganesh.penup()
ganesh.left(135)
ganesh.forward(100)

ganesh.pendown()
ganesh.fillcolor("#AE3509")
ganesh.begin_fill()
ganesh.left(-90)
ganesh.circle(90,180)
ganesh.left(90)
ganesh.pendown()
ganesh.forward(180)
ganesh.end_fill()
ganesh.penup()

ganesh.fillcolor("yellow")
ganesh.begin_fill()
ganesh.backward(90)
ganesh.right(45)
ganesh.pendown()
ganesh.circle(-60,90)
ganesh.right(90)
ganesh.circle(-60,90)
ganesh.end_fill()





