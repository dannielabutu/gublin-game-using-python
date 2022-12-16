import random
#importing random modules so the user does not guess right

number_of_doors = 5
#assigning the number of doors to 5

print("welcome to the angry goblin hunt")
print("an award-winning game full of adventure and excitement(!)")
#this is the introduction message of the game


#asking the player to input his name
player_name = input("What is your name? ")
print(player_name + ", can you find the goblin?")

print("|_|" * number_of_doors)

goblin_position = random.randint(1, number_of_doors)

#assigning a variable to true so that the user keeps trying
keep_trying = True

#main game loop
while keep_trying:
    guessed_position = input("Can you guess where the gublin is hiding? ")
#converting the the guessed position into an integer to have a different answer
    guessed_position = int(guessed_position)

    if guessed_position == goblin_position:
        print("Well done. you found where the goblin is hiding")
        keep_trying = False
#if the user gets the answer the value of keep trying changes to false

    else:
            print("No the goblin is still hiding somewhere. ")
print("Thank you for playing. See you next time")