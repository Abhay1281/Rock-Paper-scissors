import random 
actions = ["Rock","Paper","scissors"]
again = True
while again : 
    print(random.choice(actions))
    another_roll = input("Want to play again? (y/n):")
    if another_roll.lower() == "y":
     continue 
    else: 
        break