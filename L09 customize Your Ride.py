#Asking for mode of transport
print("1.Car")
print("2.Bike")
choice = int(input("Select one of the two: "))
print()

#Asking for further choices
if choice == 1:
    print("1.SUV\n"+"2.Sedan")
    choice2 = int(input("Select one of the two: "))
    if choice2 == 1:
        print("Your SUV is on the way!")
    elif choice2 == 2:
        print("Your Sedan is on the way!")
    else:
        print("Invalid choice.")
elif choice == 2:
    print("1.Mountain bike\n"+"2.Desert bike")
    choice2 = int(input("Select one of the two: "))
    if choice2 == 1:
        print("Your Mountain bike is on the way!")
    elif choice2 == 2:
        print("Your Desert bike is on the way!")
    else:
        print("Invalid choice.")
else:
    print("We only have cars and bikes. Invalid choice.")