import turtle
import time
speed=float(input("Input an integer for wall build speed.\n(recommended ~10) --> "))
size=int(input("Input an integer for brick sizes.\n(recommended ~3) --> "))

# Defines the brick-laying patterns to flip-flop between both.
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
    
# Reset the turtle to a starting position just below the previous set.
def setupcontinue():
        turtle.right(90)
        turtle.forward(size*10)
        turtle.left(90)
        turtle.backward(size*160)
   

# Defines the brick creation process to easily continue off a previous brick.
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


def main():
    turtle.penup()
    turtle.speed(speed)
    turtle.teleport(-100*size,100*size)
    turtle.pendown()
    for i in range(8):
        firstpattern()
        secondpattern()
    turtle.done
    input("Brick wall finished! Press enter here to close.")

main()