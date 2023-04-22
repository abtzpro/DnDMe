import random
import json

class Character:
    def __init__(self):
        self.name = ""
        self.race = ""
        self.job = ""
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        
    def assign_stats(self):
        stats = []
        for i in range(6):
            rolls = [random.randint(1, 6) for j in range(4)]
            rolls.remove(min(rolls))
            stat = sum(rolls)
            stats.append(stat)
        self.strength = stats[0]
        self.dexterity = stats[1]
        self.constitution = stats[2]
        self.intelligence = stats[3]
        self.wisdom = stats[4]
        self.charisma = stats[5]
        
    def to_dict(self):
        return {
            "name": self.name,
            "race": self.race,
            "job": self.job,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma
        }
        
    def __str__(self):
        return f"Name: {self.name}\nRace: {self.race}\nJob: {self.job}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"
        
        
def create_character():
    character = Character()
    character.name = input("Enter a name for your character: ")
    character.race = input("Enter a race for your character: ")
    character.job = input("Enter a job for your character: ")
    character.assign_stats()
    return character

def save_character(character, filename):
    with open(filename, "w") as f:
        json.dump(character.to_dict(), f)
        
def load_character(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        character = Character()
        character.name = data["name"]
        character.race = data["race"]
        character.job = data["job"]
        character.strength = data["strength"]
        character.dexterity = data["dexterity"]
        character.constitution = data["constitution"]
        character.intelligence = data["intelligence"]
        character.wisdom = data["wisdom"]
        character.charisma = data["charisma"]
        return character

def choose_option():
    choice = input("Enter '1' to create a new character, '2' to save a character, '3' to load a character, or 'q' to quit: ")
    if choice == "1":
        return create_character()
    elif choice == "2":
        filename = input("Enter a filename to save your character to: ")
        character = create_character()
        save_character(character, filename)
        return character
    elif choice == "3":
        filename = input("Enter a filename to load your character from: ")
        return load_character(filename)
    elif choice == "q":
        return None
    else:
        print("Invalid choice, please try again.")
        return choose_option()

if __name__ == "__main__":
    while True:
        character = choose_option
