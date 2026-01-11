print("Right Angle triangle Pattern")
rows = int(input("Enter the number of rows: "))

for row in range(rows):
    for column in range(row+1):
        print("*",end="")
    print()

