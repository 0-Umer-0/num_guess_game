# number guessing game

import random
original_number = random.randint(0,99)
attempt = 0
while True:
 guessed_number = int(input("guess the number: "))
 attempt+=1

 if(guessed_number < original_number):
    print("your guess is too low")
 elif(guessed_number > original_number):
    print("your guess is too high")
 else:
  print(f"your guess is correct and you attempted in {attempt} attempts")
  break
 



