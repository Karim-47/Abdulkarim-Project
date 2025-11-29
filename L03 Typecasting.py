#Assigning values to var

Name="Abdulkarim"
Age= 17
Weight= 55.6 
Is_Student= True

#Displaying orignial data types
print("ORIGINAL DATA TYPES:\n")
print(f"The data type for name {Name} is: ",type(Name),
      f"\nThe data type for age {Age} is:",type(Age),
      f"\nThe data type for weight {Weight} is:",type(Weight),
      f"\nThe answer to the uncertainity IS_Student is {Is_Student}",type(Is_Student))

#Typecasting
print(f"The new data type for age {Age} is:",type(float(Age)))
print(f"THE new data type for weight {Weight} is:",type(int(Age)))