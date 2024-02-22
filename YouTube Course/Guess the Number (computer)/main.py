import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c" and low != high:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)")

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print (f"The computer guessed your number, it is {guess}")

if __name__ == "__main__":
    computer_guess(1000)