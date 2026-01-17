num = int(input("Enter the number for binary converison: "))

binary = ""

while num >0:
    if num % 2 ==0:
        binary= "0" + binary 
    else:
        binary= "1" + binary 
    num = num//2

if len(binary)<8:
    for i in range((8-len(binary))):
        binary = "0" + binary

print(binary)