def circumference(radius):
    pi = 3.14159
    area = 2*pi*radius
    return area


r = int(input("Enter the radius of the circle whose area you want to calculate: "))

Area = round(circumference(r),1)
print("The Circumference is:",Area)