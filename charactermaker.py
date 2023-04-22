import random
import pickle

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
        
    def __str__(self):
        return f"Name: {self.name}\nRace: {self.race}\nJob: {self.job}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"

def create_character():
    character = Character()
    character.name = input("Enter a name for your character: ")
    character.race = input("Enter a race for your character: ")
    character.job = input("Enter a job for your character: ")
    character.assign_stats()
    return character

def save_character(character):
    file_name = f"{character.name}.pkl"
    with open(file_name, "wb") as file:
        pickle.dump(character, file)

def load_character(file_name):
    with open(file_name, "rb") as file:
        character = pickle.load(file)
        return character

character = create_character()
print(character)

file_name = f"{character.name}.pkl"
save_character(character)

loaded_character = load_character(file_name)
print(loaded_character)
