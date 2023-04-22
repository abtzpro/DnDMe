import random

class NPC:
    def __init__(self, name, level, strength, dexterity, constitution, intelligence, wisdom, charisma, armor_class, hit_points, damage_die, damage_bonus):
        self.name = name
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.armor_class = armor_class
        self.hit_points = hit_points
        self.damage_die = damage_die
        self.damage_bonus = damage_bonus
    
    def attack(self, target):
        hit_roll = random.randint(1, 20) + self.level
        if hit_roll >= target.armor_class:
            damage_roll = random.randint(1, self.damage_die) + self.damage_bonus
            target.hit_points -= damage_roll
            print(f"{self.name} hit {target.name} for {damage_roll} damage!")
        else:
            print(f"{self.name} missed {target.name}!")
    
    def __str__(self):
        return f"{self.name} (Level {self.level}) - STR: {self.strength} | DEX: {self.dexterity} | CON: {self.constitution} | INT: {self.intelligence} | WIS: {self.wisdom} | CHA: {self.charisma} | AC: {self.armor_class} | HP: {self.hit_points} | Damage: {self.damage_die} + {self.damage_bonus}"
