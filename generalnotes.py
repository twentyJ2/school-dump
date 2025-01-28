import turtle
turtle.speed(1)
overarchIncrements=3
distance=0
while overarchIncrements>0:
    distance+=100
    increments=4
    while increments>0:
     turtle.forward(distance)
     turtle.right(90)
     increments-=1
    turtle.left(90)
    overarchIncrements-=1
turtle.done()

'''print(1,2,3,sep="canbeanything")
print(2, end="alsowhatever")
print(3,end="!!\n")'''


'''capacity=int(input("Input SU capacity: "))
mult=0
rpm=0
reduction=0

while capacity>0:
    rpm=int(input("Input RPM: "))
    mult=int(input("Input SU mult: "))
    reduction=int(rpm*mult)
    capacity-=reduction
    print("You have",str(capacity),"SU capacity remaining.")
print("No more SU capacity remaining. ("+str(capacity)+")")

.isnumeric()'''