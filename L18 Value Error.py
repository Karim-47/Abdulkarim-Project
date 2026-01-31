try :
    num = float(input("Enter a number: "))
    print("The number entered is",num)
except ValueError as ve:
    print("There was a value exception error:",ve)

print("I am outside the try and except block.")