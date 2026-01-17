Num = input("Enter the number: ")
digits=0
count = 0
while count< len(Num):
    if Num[count]>="0" and Num[count]<="9":
        digits +=1
    count+=1

print(f"Your number has {digits} digits.")
