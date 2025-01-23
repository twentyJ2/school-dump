print("Number to Roman Numeral.\nInput Number.")
userNum=int(input())
# I, II, III, IV, V, VI, VII, VIII, IX, X, XI...
# 1,  2,   3,  4, 5, 6,  7,   8,    9, 10, 11...
# IV/IX booleans defined as Integers for easy multiplication of strings.
endresult="ERR"
ixNum=0
vNum=0
ivNum=0
iNum=0
xNum=int(userNum/10)
remainder=userNum%10
if remainder==9:
    ixNum=1
else:
    if remainder>=5:
        vNum=1
        iNum=remainder%5
    if remainder==4:
            ivNum=1
    else:
        iNum=remainder%5
endresult=("IX"*ixNum+"X"*xNum+"IV"*ivNum+"V"*vNum+"I"*iNum)
print(endresult)