import random
def user_guess(x):
    random_number = random.randint(1, x)
    guess = 0
    
    while random_number != guess:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if random_number > guess:
            print ("Sorry, guess again. Too low.")
        elif random_number < guess:
            print ("Sorry, guess again. Too high.")

    print (f"Congrats. You have have guess the number {random_number}")

if __name__ == "__main__":
    user_guess(10)