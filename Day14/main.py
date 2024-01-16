import random
import game_data
import art

def get_random_user(used_people):
    new_person = False

    while not new_person:
        person = random.choice(game_data.data)
        if person in used_people:
            continue
        used_people.append(person)
        new_person = True
    return person
        

def game():
    print(art.logo)
    used_people = []
    game_over = False
    score = 0
    person_a = get_random_user(used_people)
    person_b = get_random_user(used_people)

    while not game_over:
        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
        print(art.vs)
        print(f"Compare B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

        user = input("Who has more followers? Type 'A' or 'B: ").upper()

        if user == 'A' and person_a['follower_count'] > person_b['follower_count']:
            score += 1
            person_b = get_random_user(used_people)
            print(f"You are right! Current score: {score}")
        elif user == 'B' and person_b['follower_count'] > person_a['follower_count']:
            score += 1
            person_a = get_random_user(used_people)
            print(f"You are right! Current score: {score}")    
        else:
            print(f"Sorry, that is wrong. Final score: {score}")
            return    

game()