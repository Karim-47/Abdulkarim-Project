#Get input for health inquiry
medical_inquiry = input("Do you have any medical issue; Y or N: ")

#get attendance percentage
attendance = int(input("Enter you attendance percentage: "))

if medical_inquiry.upper()=="Y":
    print("You are not allowed to attend the exam becasue you are unhealthy.")
else: 
    if attendance>= 75:
        print("You are allowed to attend the exam because you attendance is sufficient and you are healthy.")
    else:
        print("You are not allowed to attend the exam because your attendace is not sufficient.")