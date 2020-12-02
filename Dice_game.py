from random import randint
import time
# importing random module to provide random action
#Time module to get some time to roll the dice

selection = input(print("Do you want to improve the chances of getting more 6? \n(Y/N)"))

if selection == 'Y' or 'y':
    # Applying condition for getting more 6 on dice
    roll_dice = "Yes"
    while roll_dice == "Yes" or roll_dice =='Y' or roll_dice =='y':
        print('getting number')
        time.sleep(1)
        num = randint(3, 6)
        print(num)
    # it will give you number in between 4 to 6
        roll_dice = input('Do you want to play again? (Y/N)')

else:
# normal Dice 1 to 6
    roll_dice = "Yes"
    while roll_dice == "Yes" or roll_dice =='Y' or roll_dice =='y':
        print('getting number')
        time.sleep(1)
        Dice_number = randint(1, 6)
        # it will give you number in between 1 to 6
        print(Dice_number)
        roll_dice = input('Do you want to play again? (Y/N)')

print()
