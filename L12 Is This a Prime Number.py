lower = int(input("Enter a lower bound number: "))
upper = int(input("Enter a upper bound number: "))

print(f"The prime numbers within the range of {lower} and {upper} are: ")
temp = 0
for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)            

