rows = int(input("How many rows do you want?: "))
number = 1

print("FLOYD'S TRIANGLE")

for row in range(rows):
    for column in range(row+1):
        print(number,end="  ")
        number +=1
    print()