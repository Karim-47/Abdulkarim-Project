#getting inputs
height = float(input("Enter your height in cm: "))
weight = float(input("Enter you weight in kg: "))

#calculating BMI
BMI = weight/((height/100)**2)

#displaying results
print(f"Your BMI is {BMI}.")
#displaying status
if BMI <= 18.4 :
    print("you are underweight")
elif BMI <= 24.9 :
    print("you are healthy")
elif BMI <= 29.9 :
    print("you are overweight")
elif BMI <= 34.9 :
    print("you are severely overweight")
elif BMI <= 39.9 :
    print("you are obese")
else :
    print("you are severely obese")
