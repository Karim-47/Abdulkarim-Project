#take inputs of marks 
print("One by one enter marks out of 100 for each subject to get the percentage.")

English=int(input("Enter marks for English: "))
Maths=int(input("Enter marks for Maths: "))
Physics=int(input("Enter marks for Physics: "))
Computer=int(input("Enter marks for Computer: "))
Economics=int(input("Enter marks for Economics: "))

#Calculating Percentage
Sum=English+Maths+Physics+Computer+Economics
Percentage= int((Sum/500)*100)

#Displaying results
print(f"Your total marks are: {Sum}/500")
print(f"Your percentage is {Percentage}%")
