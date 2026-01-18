def addition(num1,num2):
    calculation = str(num1)+" + "+str(num2)+" = "+str(num1+num2)
    return calculation
def subtraction(num1,num2):
    calculation = str(num1)+" - "+str(num2)+" = "+str(num1-num2)
    return calculation
def multiplication(num1,num2):
    calculation = str(num1)+" * "+str(num2)+" = "+str(num1*num2)
    return calculation
def division(num1,num2):
    calculation = str(num1)+" / "+str(num2)+" = "+str(num1/num2)
    return calculation

print("CALCUATOR\n"+"a.Addition\n"+"b.Subtraction\n"+"c.Multiplication\n"+"d.Division\n")

choice = input("Enter your choice of operator (a/b/c/d): ")
number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
if choice == "a":
    result = addition(number1,number2)
    print(result)
elif choice == "b":
    result = subtraction(number1,number2)
    print(result)
elif choice == "c":
    result = multiplication(number1,number2)
    print(result)
elif choice == "d":
    result = division(number1,number2)
    print(result)
else:
    print("Invalid choice.")
