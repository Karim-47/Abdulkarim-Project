#getting inputs
print("Enter your marks: ")
mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())

Average = (mark1+mark2+mark3+mark4+mark5)/5
print(Average)

if Average>= 91 and Average <=100:
    print("Your grade is A1")
elif Average>= 81 and Average <91:
    print("Your grade is A2")
elif Average>= 71 and Average <81:
    print("Your grade is B1")
elif Average>= 61 and Average <71:
    print("Your grade is B2")
elif Average>= 51 and Average <61:
    print("Your grade is C1")
elif Average>= 41 and Average <51:
    print("Your grade is C2")
elif Average>= 33 and Average <41:
    print("Your grade is D")
elif Average>= 21 and Average <33:
    print("Your grade is E1")
elif Average>= 0 and Average <21:
    print("Your grade is E2")
else:
    print("Invalid input!")
