a = int(input("Enter a valid value of a speed: "))
b = int(input("Enter a valid value2 of a speed: "))
c = int(input("Enter a valid value3 of a speed: "))

avg = int((a+b+c) / 3)
print(avg)

if avg> a and avg> b and avg > c:
    print (f"{avg} is higher than {a}, {b}, {c}") 
elif avg > a and avg > b:
    print (f"{avg} is higher than {a}, {b}") 
elif avg > a and avg> c:
    print (f"{avg} is higher than {a}, {c}") 
elif avg> b and avg > c:
    print (f"{avg} is higher than {b}, {c}") 
elif avg> a:
    print(f"{avg} is just higher than {a}")
elif avg> b:
    print (f"{avg} is just higher than {b}")
elif avg> c:
    print (f"{avg} is just higher than {c}")
else:
    print("invalid input")