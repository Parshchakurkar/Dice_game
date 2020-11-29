from random import randint

# importing random module to provide random action

print("Do you want to improve the chances of getting more 6 \n")
selection = input(print("Enter Y for yes and N for No\n"))
if selection == 'Y':  # Applying condition for getting more 6 on dice
    num = randint(4, 6)
    print(num)# it will give you number in between 4 to 6
elif selection == 'N':
    Dice_number = randint(1, 6)# it will give you number in between 1 to 6
    print(Dice_number)
print()
