A = input("Enter the first number: ")
B = input("Enter the second number: ")
C = input("Enter the third number: ")

temp = A 
A = C 
C = B 
B = temp 
print("The first number is now: "+A)
print("The second number is now: "+B)
print("The third number is now: "+C)

