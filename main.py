import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([1, -1, 0])
print("Welcome to Snake Water Gun")
print("s for snake, w for water, g for gun")
youstr = (input("Enter your choice:"))
youDict = {"s":1, "w": -1, "g": 0}
reversedDict = {1:"Snake", -1:"Water", 0:"Gun"}
you = youDict[youstr]

print (f" computer chose {reversedDict[computer]}\n you chose {reversedDict[you]}")
if computer == you:
    print("It's a tie")
else:
    if computer == -1 and you == 1:
        print("You win")
    elif computer == -1 and you == 0:
        print("You lose")
        
    elif  computer == 1 and you == -1:
        print("You lose")
    elif computer == 1 and you == 0:
        print("You win")
    elif computer == 0 and you == 1:
        print("You lose")
    elif computer == 0 and you == -1:
        print("You win")

    else:
        print("Something went wrong")
