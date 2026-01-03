#Inputting the string
string = input("Enter a word to reverse: ")

reverse = ""

for i in string:
    reverse = i + reverse

print("The original string is: "+ string)
print("The reversed string is: "+ reverse)