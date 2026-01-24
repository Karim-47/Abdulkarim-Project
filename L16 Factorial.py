def factorial(num):
    if num == 0 or num==1:
        return 1
    else:
        return num * factorial(num - 1)
    

num = int(input("Enter the number whose factorial you want: "))

if num<0:
    print("Factorial for negative numbers does not exist!")
else:
    print("The factorial of",num,"is",factorial(num))