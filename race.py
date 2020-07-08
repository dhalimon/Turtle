import turtle
import random

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,100)

player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)


#Developing the Game

# Step 1: You’ll start by telling your program to check if either turtle has reached its home.
# Step 2: If they haven’t, then you’ll tell your program to allow the players to continue trying.
# Step 3: In each loop, you tell your program to roll the die by randomly picking a number from the list.
# Step 4: You then tell it to move the respective turtle accordingly, with the number of steps based on the outcome of this random selection.


#Creating the Die
die = [1,2,3,4,5,6]

for i in range(20):

    if player_one.pos() >= (300,100):

            print("Player One Wins!")

            break

    elif player_two.pos() >= (300,-100):

            print("Player Two Wins!")

            break

    else:

            player_one_turn = input("Press 'Enter' to roll the die ")

            die_outcome = random.choice(die)

            print("The result of the die roll is: ")

            print(die_outcome)

            print("The number of steps will be: ")

            print(20*die_outcome)

            player_one.fd(20*die_outcome)

            player_two_turn = input("Press 'Enter' to roll the die ")

            d = random.choice(die)

            print("The result of the die roll is: ")

            print(die_outcome)

            print("The number of steps will be: ")

            print(20*die_outcome)

            player_two.fd(20*die_outcome)

