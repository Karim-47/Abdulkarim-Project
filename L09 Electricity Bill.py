#check total units consumed
units = int(input("How many units did you consume: "))

#Calculate the price of electricity and the surcharge respective of the consumption

if units<50:
    amount = units * 2.5
    surcharge = 25
elif units<=100:
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
elif units<=200:
    amount = 130 + 162.5 + ((units - 100) * 5.25)
    surcharge = 45
else:
    amount = 130 + 162.5 + 525 + ((units - 200) * 8.45)
    surcharge = 75 

#Caluating and displaying bill
bill = amount + surcharge
print(f"Your total bill is: Rs.{bill}/-")
