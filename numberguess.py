import random
import time
random.seed(time.time())
mysteryNum=random.randint(1,10)
print(mysteryNum)
victoryCheck=False
guessCount=0
guessMin=1
guessMax=10
print("Welcome to the number guessing game.\nYou will have 3 chances to guess a mystery number between 1-10.\n\n")

for i in range(3,0,-1):
    print(f"You have {i} guess(es) left.")
    guess=input(f"Enter an integer between {guessMin}-{guessMax} --> ")
    while not guess.isnumeric() or int(guess)>guessMax or int(guess)<guessMin:
        print(f"{guess} is invalid...\n\nInput exclusively one whole number ranging from {guessMin}-{guessMax}. --> ")
        guess=input()
    guessCount+=1
    if int(guess)==mysteryNum:
            victoryCheck=True
            break
    elif int(guess)>mysteryNum:
        print("Guessed too high!\n\n")
        guessMax=int(guess)-1
    else:
        print("Guessed too low!\n\n")
        guessMin=int(guess)+1

if victoryCheck:
    print(f"Congrats! You guessed the correct number.\nGuesses taken to complete: {guessCount}")
else:
    print(f"You ran out of guesses. The correct number was {mysteryNum}.")
    
    

'''
start out with 3 guesses
generate random number
message to introduce
for loop 3 times:
 You have {inverse loopcount} guess(es) left.
 contingency to ensure an actual number is inputted
  prompt to guess
  if guess is too large, remove a count "too large"
  Too small, ditto above.
  Perfect guess, set win boolean and break

win/loss boolean:
 Victory, give victory message
 Give stats about tries taken to complete in victory msg.
 
 Loss, give loss message with mystery number and 
'''