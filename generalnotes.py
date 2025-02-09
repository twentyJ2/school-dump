import turtle
'''
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
    '''
'''print(1,2,3,sep="canbeanything")
print(2, end="alsowhatever")
print(3,end="!!\n")'''


'''capacity=int(input("Input SU capacity: "))
mult=0
reduction=0

while capacity>0:
    rpm=input("Input RPM: ")
    while rpm.isnumeric() == False:
        rpm=input("Input a numeric this time: ")
    mult=int(input("Input SU mult: "))
    reduction=int(rpm*mult)
    capacity-=reduction
    print("You have",str(capacity),"SU capacity remaining.")
print("No more SU capacity remaining. ("+str(capacity)+")")
'''

'''
sum=0.0
addition=1.0
print("Input numbers to add to the sum.\nInput 0 to end prompt and show sum.\n")
while addition!=0:
    addition=float(input())
    sum+=addition
print(sum)
'''
side_length=100
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    print("cool, all done")
draw_square()
for size in range(25,151,25):
    draw_square(size)

turtle.done()
