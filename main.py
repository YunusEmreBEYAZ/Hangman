import random
from random_cars import word_list
from hangman_lives import stages


chosen_word = random.choice(word_list)
lives = 6

display = []
for i in range(len(chosen_word)):
    display += "_"
end_of_the_game = False

# print(chosen_word)
print("Welcome to the Hangman game! You can start guessing a car when you are ready!\n")


while not end_of_the_game: 

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}. Try again!")
        
    for n in range(len(chosen_word)):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = letter
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. You lost a life!")
        print(stages[lives])

    print(display)

    if "_" not in display and lives > 0:
        end_of_the_game = True
        print(f"The word was {chosen_word}")
        print("You win!")
    elif lives == 0:
        end_of_the_game = True
        print("You lose!")
        print(f"The word was {chosen_word}")
        print(stages[0])

    