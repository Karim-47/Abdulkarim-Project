import random as r
num = r.randint(10,20)

print("A random number from 10 to 20 would be generated and you have to guess it to win.")

while True:
    guess=int(input("Give me your best guess: "))
    print()
    if guess == num:
        print("You won!")
        print(f"The number was {num}")
        break

    else:
        print("Wrong guess try again!")
