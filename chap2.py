itemPrice=float(input("Input the item's baseline price: "))
totalTax=round(float(itemPrice*0.025+itemPrice*0.05),2)
totalIP=round(totalTax+itemPrice,2)
# A little decimal trimming with round() for the end result to look cleaner with a more realistic price.

print("Price of your item:",str(itemPrice),"\nCounty sales tax: 2.5%; $"+str(itemPrice*0.025)+"\nState sales tax: 5%; $"+\
    str(itemPrice*0.05)+"\nTotal tax: $"+str(totalTax)+"\nTotal price including taxes: $"+str(totalIP))