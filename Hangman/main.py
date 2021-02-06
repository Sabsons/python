#Modules
import random
import hangman_words
import hangman_art

#Pick a random word from the word_list in hangman_words.py
chosen_word = random.choice(hangman_words.word_list)

#Variables
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Print the starting logo from hangman_art.py
print(hangman_art.logo)

#Create the display list and make it list "_" equal to the number of letters in the random word picked.
display = []
for _ in range(word_length):
    display += "_"

#Main loop of game
#Ask the user for a letter and make it lower.
while not end_of_game:
    guess = input("Guess a letter: ").lower()


    #If the user already entered the letter before
    if guess in display:
      print(f"You already guessed the letter {guess}.")

    #Loop inside the word and change the blanks to the corresponding correct letter.
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    #If the letter is wrong: tell the user, remove a life, and if lives = 0 Tell the user that he lost and what the word was.
    if guess not in chosen_word:

        print(f"{guess} is not is a letter in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You wasted all your lives and lost.")
            print(f"The word was {chosen_word}.")

    #print the word
    print(f"{' '.join(display)}")

    #If all the blanks are gone with lives remaining tell the user that he won.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print the current art that corresponds to the remaining lives of the user.
    print(hangman_art.stages[lives])