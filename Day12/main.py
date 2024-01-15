import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
num_list = ["_" for x in range(1, 101)]

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def change_num_list(num, up_down):
    global num_list

    
    if up_down == '+':
       change = range(num, 101, 1)
    else:
       change = range(1, num + 1, 1)

    for x in change:
       num_list[x - 1] = x

    print(' '.join(str(x) for x in num_list))

def check_answer(guess, answer):
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
    elif guess > answer:
        print(f"Too high.")
        change_num_list(guess, '+')
        return -1
    elif guess < answer:  
        print(f"Too low.")
        change_num_list(guess, '-')
        return -1

def game():

    print("Welcome to the Number Guessing Game!")
    print("I am thinking in a number between 1 and  100.")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns += check_answer(guess, answer)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
