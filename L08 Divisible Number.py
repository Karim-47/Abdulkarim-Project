Numerator = int(input("Enter the numerator: "))
Denominator = int(input("Enter the denominator: "))

if Numerator%Denominator==0:
    print(f"{Numerator} is fully divisible by {Denominator}.")
else:
    print(f"{Numerator} is not fully divisible by {Denominator}.")