# Project Scope: Guessing Game

# Select correct word from list of 7-letter words. 3 attempts to guess.

# On incorrect guess, give number of correct characters in correct position

# Requirements:
# Be able to check guess against list of options
# Be able to compare guess and answer using character and position
# Count numer of correct characters in position
# Limit to 3 attempts



def evalGuess(guess):
	correct = 0

	for l in guess:
		if guess.find(l) == answer.find(l):
			correct = correct + 1

	print(correct)

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

answer = wordList[0]

guess = input("Can you guess the word?\n")

guess = [word for word in wordList if guess == word]

if guess == []:
	print("That is not one of the words")
if guess[0] == answer:
	print("YOu win!")
else:
	evalGuess(guess[0])