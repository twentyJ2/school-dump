import turtle
turtle.penup()
speed=float(input("Input an integer for wall build speed.\n(recommended ~10) --> "))
turtle.speed(speed)
size=int(input("Input an integer for brick sizes.\n(recommended ~3) --> "))
turtle.teleport(-100*size,100*size)
turtle.pendown()
def setupcontinue():
        turtle.right(90)
        turtle.forward(size*10)
        turtle.left(90)
        turtle.backward(size*160)
        
def firstpattern():
        turtlesquare()
        for i in range(7):
            turtlebrick()
        turtlesquare()
        setupcontinue()
    
def secondpattern():
    for i in range(8):
        turtlebrick()
    setupcontinue()


def turtlesquare():
    turtle.forward(size*10)
    for i in range(4):
        turtle.right(90)
        turtle.forward(size*10)
def turtlebrick():
    turtle.forward(size*20)
    for i in range(2):
        turtle.right(90)
        turtle.forward(size*10)
        turtle.right(90)
        turtle.forward(size*20)

for i in range(8):
    firstpattern()
    secondpattern()

turtle.done
