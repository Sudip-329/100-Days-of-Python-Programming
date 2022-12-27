# Auth : Sudip Chakrabarty
# Date : 27.12.2022
# Kalinga Institute of Inustrial Technology
# It is simple higher lower game where player will guess who is more famous between two person ,if the
# guess is right, his/her score will be increased...


print("WELCOME TO THE HIGHER LOWER GAME !!!")
from logo_higher_lower import logo
from logo_higher_lower import logo2
import os

from game_data_higher_lower import data
import random

def format_data(account):
    """Takes the account data and returns printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a { account_desc}, from { account_country}"


#Follower count check answer function
def check_answer(guess,a_followers,b_followers):
    if a_followers > b_followers:        #menas if a is bigger and user guess is also a then its true.
        return guess == "a"
    else:
        return guess == "b"   # means if b is bigger and user guess is also b then return this as true.
 
#Display art.
print(logo)
score = 0

game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #Generate a random account.(data )
    account_a =account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A : {format_data(account_a)}")
    print(logo2)
    print(f"Against B : {format_data(account_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? A or B?").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    #give user feedback on their guess
    os.system('cls')
    print(logo)

    if is_correct:
        score +=1
        print(f"You are right! Current score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that is wrong! FInal sscore : {score}")