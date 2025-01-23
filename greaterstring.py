userStringA=input("String value comparing\nInput first string: ")
userStringB=input("Input second string: ")
if userStringA > userStringB:
    print(userStringA)
else:
    if userStringA == userStringB:
        print("tie")
    else:
        print(userStringB)
        
# Value determined by sum of letters converted to ASCII? (a>A, to decimal, 97>65)