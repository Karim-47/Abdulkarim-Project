num = input("Enter a number: ")
length=len(num)
if length >=4:
    even = 0
    if (length%2)==0:
        even=1

    if even:
        mid1 = int(num[(int(length/2))-1])
        mid2 = int(num[int(length/2)])
        product = mid1  * mid2     

    if not even:
        mid1 = int(num[int(length//2)])
        mid2 = int(num[int(length//2)+1])
        product = mid1 * mid2

    print(f"The product of mid digits is ({mid1} * {mid2} = {product})")
else:
    print("It is not a 4-digit number.")
