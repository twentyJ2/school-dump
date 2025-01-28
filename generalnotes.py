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

for num in [0,1,2,3]:
    print(num)
    
for gog in range(4):
    print(gog)
    
for wow in range(90,100):
    print(wow)
    
for examp in range(90,100,2):
    print(examp)
    
for anex in range(10,0,-1):
    print(anex)
    
for gunk in range(10):
    if (gunk==3):
        break
    print(gunk)
    
for num in range(10):
    if num % 2 ==0:
        continue
    print(num)
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