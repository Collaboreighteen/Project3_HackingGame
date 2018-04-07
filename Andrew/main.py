import random
import emoji

seedWordDict = [
	"AARRGHH",
	"ABACTOR",
	"ABALONE",
	"ABANDED",
	"ABANDON",
	"ABASERS",
	"ABASHED",
	"ABASHES",
	"ABASIAS",
	"ABASING",
	"ABATERS",
	"ABATING",
	"ABATORS",
	"ABATTIS",
	"ABATURE",
	"ABAXIAL",
	"ABAXILE",
]

emojiSeedList = list(emoji.EMOJI_LIST.values())



def getRandomItem(list):
	return random.choice(list)


def addToList(list, seedList):
	proposedWord = getRandomItem(seedList)
	list.append(proposedWord)

def addToUniqueList(list, seedList):
	proposedWord = getRandomItem(seedList)
	if proposedWord not in list:
		list.append(proposedWord)
	else: 
		addToList(list, seedList)

def createRandomList(count, seedList):
	returnList = []

	while len(returnList) < count:
		addToList(returnList, seedList)

	return returnList

def createUniqueRandomList(count, seedList):
	returnList = []

	while len(returnList) < count:
		addToUniqueList(returnList, seedList)

	return returnList



def getLikeCharsCount(choice, answer): 
	charIdx = (len(answer) - 1)
	correctCount = 0
	while(charIdx >= 0):
		if(choice[charIdx] == answer[charIdx]):
			correctCount = correctCount + 1
		charIdx = charIdx - 1

	return correctCount

def guessesRemainingDisplay(guesses):
	returnStr = "Remaining Guesses: "
	for i in range(guesses):
		returnStr = returnStr + ' #'

	return returnStr

def insertWordsIntoDisplayList(charList, insertWords):
	for i in insertWords:
		index = random.randrange(0, len(charList))
		charList[index] = ' ' + i

	return charList



# Da fuq, I don't understand list comprehension :|
def chunks(l, n):
    n = max(1, n)
    return list(l[i:i+n] for i in range(0, len(l), n))

def printToWidth(string, width):
	rows = chunks(string, width)
	for i in rows:
		print("".join(i)) 

def generateDisplay(words, guesses):
	print(guessesRemainingDisplay(guesses))
	dispalyChars = createRandomList(1000, emojiSeedList)
	displayCharsWithWords = insertWordsIntoDisplayList(dispalyChars, words)



	printToWidth(' '.join(displayCharsWithWords), 50)

def init(guesses, choices):
	wordList = createUniqueRandomList(choices, seedWordDict)
	ANSWER = getRandomItem(wordList)
	guessesRemaining = guesses
	generateDisplay(wordList, guessesRemaining)
	
	while(guessesRemaining > 0):
		guess = input()
		correctChars = getLikeCharsCount(guess, ANSWER)
		totalChars = len(ANSWER)
		print(str(correctChars) + '/' + str(totalChars) + ' correct')
		if(correctChars == totalChars):
			print('Ya Did it')
			guessesRemaining = -1
		else:
			guessesRemaining = guessesRemaining - 1
			print(guessesRemainingDisplay(guessesRemaining))

GUESSES = 3
WORDCHOICES = 5

init(GUESSES, WORDCHOICES)

