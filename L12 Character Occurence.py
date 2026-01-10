string = input("Enter a word or a sentence: ")

char = input("Enter the character you want to search: ")

char_count = 0
for i in range(len(string)):
    if string[i] == char:
        char_count += 1
    
print(f"The character {char} has occured {char_count} times in the string {string}.")