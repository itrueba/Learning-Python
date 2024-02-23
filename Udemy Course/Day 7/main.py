#Password Generator Project
import random

from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
end_of_game = False

display = []
chosen_letter = set()

for _ in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display or guess in chosen_letter:
        print(f"You've already guessed {guess}")
        continue

    chosen_letter.add(guess)

    for letter in range(word_length):
        if guess == chosen_word[letter]:
            display[letter] = chosen_word[letter]
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.") 
        lives -= 1
        if not lives:
            print("You lose.")
            end_of_game = True

    print(f"Chosen letter: {''.join(chosen_letter)}")
    
    print(f"Display: {''.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(stages[lives])