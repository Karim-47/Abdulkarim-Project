def cube(num):
    return num*num*num

def bythree(num):
    if num%3==0:
        return cube(num)
    else:
        return False
    
x = int(input("Enter the number1: "))
y = int(input("Enter the number2: "))

print(bythree(x))
print(bythree(y))