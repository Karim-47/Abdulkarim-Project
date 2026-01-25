word = input("Enter a word either with or without 'A': ")

for i in word:
    if i == 'A':
        print("A is found.")
        break
    else:
        print("A is not found.")