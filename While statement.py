# While statement
increment=-1
while increment<10:
    increment+=1
    print(increment)
    
for num in range(50):
    if num%2==0:
        continue
    if num>=15:
        break
    print(num)