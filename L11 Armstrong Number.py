num= int(input("Enter the number you want to check: "))
num_str = str(num)
power = len(str(num))
sum= 0
count = 0
while count<power:
    sum+= int(num_str[count])**power
    count+=1

if sum==num:
    print("This number is an Armstrong number!")
else:
    print("This number is not an Armstrong number.")
