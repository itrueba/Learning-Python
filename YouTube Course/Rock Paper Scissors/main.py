import random

def play():
    mylist = ["r", "p", "s"]
    computer = random.choice(mylist)
    print(computer)
    player = input("What is your choice? rock (R), paper (P) or scissors (S): ")

    if (player == computer):
        return "It is a tie"
    if (is_win(player, computer)):
        return "You won"
    return "You lost"

def is_win(p, c):
    if (p == "r" and c == "s" or p == "s" and c == "p" or p == "p" and c == "r"):
        return 1
    return 0

if __name__ == "__main__":
    print(play())