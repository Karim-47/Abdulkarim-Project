Alphabets= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

char = input("Enter a character to check if it is an alphabet: ").lower()

if char in Alphabets:
    print("Yes your character is an alphabet."
          )
else:
    print("No the character isn't an alphabet.")