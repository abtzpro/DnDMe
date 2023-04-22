import random

# Function to emulate rolling a dice
def roll_dice(dice_type):
    return random.randint(1, dice_type)

# Function to handle the user input and roll the dice
def roll():
    # Get the dice type from the user
    dice_type = input("What type of dice would you like to roll? (d4, d6, d8, d10, d12, d20): ")
    while dice_type not in ["d4", "d6", "d8", "d10", "d12", "d20"]:
        dice_type = input("Invalid dice type. Please choose one of the following: d4, d6, d8, d10, d12, d20: ")
    dice_type = int(dice_type[1:])

    # Get the number of dice to roll from the user
    num_dice = input("How many dice would you like to roll? ")
    while not num_dice.isdigit():
        num_dice = input("Invalid input. Please enter a number: ")
    num_dice = int(num_dice)

    # Roll the dice
    rolls = []
    for i in range(num_dice):
        rolls.append(roll_dice(dice_type))

    # Print the results
    print(f"You rolled {num_dice}d{dice_type}: {rolls}")
    print(f"The total is: {sum(rolls)}")

# Call the roll function
roll()
