#getitng input
Num = int(input("Enter a number: "))

#Comparing
if Num <= 15:
    print("The number is less than or equal to 15.\n"+
          "I am in the IF block.")
    if Num % 2 == 0:
        print("The number is EVEN.")
    else:
        print("The number is ODD.")
else:
    print("The number was greater than 15.\n"+
          "I am in the ELSE block.")
    
print("I am neither in the IF block nor in the ELSE block.")
    