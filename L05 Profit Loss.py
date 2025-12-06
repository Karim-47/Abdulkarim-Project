#Getting the figures
Cost = int(input("Enter the cost of the product: $"))
Sale_Price = int(input("Enter the amount for which you sold it: $"))

#declaring profit or loss
if Sale_Price > Cost:
    print("You made a profit!")
    print("You made a profit of",Sale_Price-Cost)
else:
    print("Unfortunately no profit.")