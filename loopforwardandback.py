# loop forward and back
# First loop goes backwards with a for loop, from 100 to "1"
sum=0
for num in range(101,1,-1):
    if num % 2 !=0:
        continue
    sum+=num
    print(num)
print("(For) sum is",sum)
    
# Now forwards using a while loop
sum=0
increment=0
while increment<101:
    increment+=1
    if increment % 2 != 0:
        continue
    print(increment)
    sum+=increment
print("(While) sum is",sum)