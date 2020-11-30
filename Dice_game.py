from random import randint

# importing random module to provide random action

print("Do you want to improve the chances of getting more 6 \n")
selection = str(input(print("Enter Y for yes and N for No\n")))
if selection == 'Y' or 'y':
    # Applying condition for getting more 6 on dice
    while True:
        next = input(print("play again enter Y"))
        if next == 'Y' or 'y':
            num = randint(3, 6)
            print(num)
            # it will give you number in between 4 to 6
        else:
            break


else:
    # normal Dice 1 to 6
    while True:
        next = input(print("play again enter Y"))
        if next == 'Y' or 'y':
            Dice_number = randint(1, 6)
            # it will give you number in between 1 to 6
            print(Dice_number)
        else:
            break
    print()
