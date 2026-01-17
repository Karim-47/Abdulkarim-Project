print("REVERSED TRIANGLE")
rows = int(input("Enter the number of rows you want: "))

for row in range(1, rows+1):
    for spaces in range(rows-row):
        print(" ",end=" ")
    for column in range(row):
        print("*",end=" ")
    print()

