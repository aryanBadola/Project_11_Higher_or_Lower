from art import logo, vs
from game_data import data
import random


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_should_continue = True

randomAccountB = random.choice(data)

while game_should_continue:

    randomAccountA = randomAccountB
    randomAccountB = random.choice(data)

    while randomAccountA == randomAccountB:
        randomAccountB = random.choice(data)

    print(f"Compare A: {randomAccountA['name']}, a {randomAccountA['description']}, from {randomAccountA['country']}")

    print(vs)

    print(f"Against B: {randomAccountB['name']}, a {randomAccountB['description']}, from {randomAccountB['country']}")

    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    a_follower_count = randomAccountA["follower_count"]
    b_follower_count = randomAccountB["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! Current Score : {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score : {score}")
