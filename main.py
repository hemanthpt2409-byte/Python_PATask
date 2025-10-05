# Task 2 :Guess the numberr game
import random

print("Welcome to the guess game")

#variables
guess_number = random.randint(1,10)
attempts=0

#loop for the guessing
while True:
     guess=(int(input("Enter your guess :")))
     attempts=attempts+1

#condition to check the guess
     if(guess<guess_number):
         print("Too Low")
     elif(guess>guess_number):
         print("Too High")
     else:
         print(f"Congrats! You guessed the number {guess_number} in {attempts} attempts.")
         break

#Task 2: Scrambled word game
#list of words
words = ["python", "javascript", "java" , "automation" , "pytest", "guvi" , "selenium"]

#selecting a word
print("Words Available", words)
choose_word= input("choose a word from the above list:")

#reverse the string
scrambling= choose_word[::-1]
print("Scrambled word is", scrambling)

#loop for guessing the word
while True:
    guess= input("Guess the original word:")
    if(guess == choose_word):
        print("Super !you found")
        break
    else:
        print("Wrong guess")