'''import turtle
turtle.speed(1)
turtle.forward(250)
turtle.right(144)
turtle.forward(250)
turtle.right(144)
turtle.forward(250)
turtle.right(144)
turtle.forward(250)
turtle.right(144)
turtle.forward(250)
turtle.done()'''

'''print(1,2,3,sep="canbeanything")
print(2, end="alsowhatever")
print(3,end="!!\n")'''


capacity=int(input("Input SU capacity: "))
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
'''
.isnumeric()'''