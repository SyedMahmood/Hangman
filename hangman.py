#This is an implementation of the traditional game Hangman. Users can enter a word, and have a partner guess a certain amount of times.

print("Hello! Welcome to Hangman!")

guesses_remaining = int(raw_input("Please state how many guesses you want your partner to have: "))

word = str(raw_input("Please enter the word that your partner will guess: ")).lower()

for i in range(25):
	print " "

guesses = ""

print "Okay, now it is time for the partner to guess! You have a maximum of ten guesses!"

guessed = '_' * len(word)
print guessed

def replaceLetter(word, index, letter):
	first = word[0:index]
	last = word[index+1:]
	return first + letter + last

while guessed != word and guesses_remaining >= 0:
	letter = str(raw_input()).lower()
	
	for index in range(len(word)):
		if letter == word[index]:
			guessed = replaceLetter(guessed, index, letter)
	
	guesses = guesses + " " + letter;
	print "Guesses: " + guesses
	print guessed
	
	if guessed == word:
		print "You won!"
		break
	
	print "Guesses remaining: " + str(guesses_remaining)
	guesses_remaining -= 1

else:
	print "Sorry, you lost!"



