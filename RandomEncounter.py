import random

# Define a list of possible events and encounters
events = ["A band of goblins attack the party", "A friendly merchant offers to trade with the party", "The party finds a hidden treasure chest", "The party stumbles upon an abandoned village", "A group of adventurers offers to join forces with the party"]

# Define a function to randomly select and return an event from the list
def get_random_event():
    return random.choice(events)

# Define a list of possible encounter types
encounter_types = ["Combat", "Social", "Exploration"]

# Define a function to randomly select and return an encounter type from the list
def get_random_encounter_type():
    return random.choice(encounter_types)

# Define a function to generate a random encounter based on the chosen encounter type
def generate_encounter(encounter_type):
    if encounter_type == "Combat":
        return "The party encounters a group of hostile creatures and must fight to survive."
    elif encounter_type == "Social":
        return "The party meets a group of friendly NPCs who offer to help them on their quest."
    elif encounter_type == "Exploration":
        return "The party discovers a hidden cave system filled with treasure and danger."

# Define a function to randomly select and return an encounter
def get_random_encounter():
    encounter_type = get_random_encounter_type()
    encounter = generate_encounter(encounter_type)
    return encounter

# Test the functions by printing out a random event and encounter
print("Random event:", get_random_event())
print("Random encounter:", get_random_encounter())
