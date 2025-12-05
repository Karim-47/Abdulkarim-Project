#Getting the amount
Amount = int(input("Enter the amount in dollars:"))

#Calculating number of notes
notes_100 = Amount // 100
notes_50 = (Amount%100) //50
notes_10 = ((Amount%100)%50) //10
notes_1 = (((Amount%100)%50)%10)

#Outputting the number of each note
print(f"The number of $100 bills is: {notes_100}\n"+
      f"The number of $50 bills is: {notes_50}\n"+
      f"The number of $10 bills is: {notes_10}\n"+
      f"The number of $1 bills is: {notes_1}")
