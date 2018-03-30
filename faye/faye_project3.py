# Project Scope: Guessing Game

# Select correct word from list of 7-letter words. 3 attempts to guess.

# On incorrect guess, give number of correct characters in correct position

# Requirements:
# Be able to check guess against list of options
# Be able to compare guess and answer using character and position
# Count numer of correct characters in position
# Limit to 3 attempts

import random

def evalGuess(guess):
	correct = 0

	for l in guess:
		if guess.find(l) == answer.find(l):
			correct = correct + 1

	print("You have "+str(correct)+"/7 correct")

wordList = [
	"provide",
	"setting",
	"cantina",
	"cutting",
	"hunters",
	"survive",
	"hearing",
	"hunting",
	"realize",
	"nothing",
	"overlap",
	"finding",
	"putting"
]

answer = random.choice(wordList)
print(answer)

guessNum = 0
end = False

print(wordList)

while (guessNum < 3 and end != True):
	guessLeft = 3 - guessNum

	if guessLeft == 3:
		guess = input("You have 3 tries to guess the word from this list. Enter your first guess\n")
	else:
		guess = input("Try again. You have " + str(guessLeft) + " guesses left\n")

	guess = [word for word in wordList if guess == word]

	if guess == []:
		print("That is not one of the words. You have " + str(guessLeft - 1) + " guesses left\n")

	if guess != []:
		if guess[0] == answer:
			print("YOu win!")
			end = True
		else:
			evalGuess(guess[0])
			
	guessNum = guessNum + 1

print("Game over!\nThe answer was " + str(answer))