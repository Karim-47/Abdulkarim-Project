#getting temperature input
Temp = float(input("Enter the outside temperature in degree celcius: "))

if Temp < 10.0:
    print("You should wear warm clothes.")
else:
    print("You may wear light clothes.")