from random import randint
import time


# importing random module to provide random action
# Time module to get some time to roll the dice


def roll_over(x, y):
    time.sleep(1)
    result = randint(x, y)
    return result


selection = input("Do you want to improve the chances of getting more 6? \n(Y/N)")

if selection == 'Y' or selection == 'y':
    # Applying condition for getting more 6 on dice
    roll_dice = "Yes"
    while roll_dice == "Yes" or roll_dice == 'Y' or roll_dice == 'y':
        print('getting number')
        num = roll_over(3, 6)
        #will give number within 3 to 6
        print(num)
        if num == 6:
            # If you get 6 it will run again and give number from1 to 6
            replay = input('Play again press Enter')
            replay_num = roll_over(1, 6)
            print(replay_num)
            while replay_num == 6:
                # If you get 6 it will run again and give number from1 to 6
                replay = input('Play again press Enter')
                replay_num = roll_over(1, 6)
                print(replay_num)
        # it will give you number in between 3 to 6
        roll_dice = input('Do you want to play again? (Y/N)')

else:
    # normal Dice 1 to 6
    roll_dice = "Yes"
    while roll_dice == "Yes" or roll_dice == 'Y' or roll_dice == 'y':
        num = roll_over(1, 6)
        #will give number within 1 to 6
        print(num)
        if num == 6:
            replay = input('Play again press Enter')
            replay_num = roll_over(1, 6)
            # If you get 6 it will run again and give number from1 to 6
            print(replay_num)
            while replay_num == 6:
                replay = input('Play again press Enter')
                replay_num = roll_over(1, 6)
                # If you get 6 it will run again and give number from1 to 6
                print(replay_num)
        roll_dice = input('Do you want to play again? (Y/N)')

print()
