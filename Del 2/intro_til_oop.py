import random

class Character:

    def __init__(self, name, level, hp, mana):
        self.name_atr = name
        self.level_atr = level
        self.hp_atr = hp
        self.mana_atr = mana
    
    def get_info(self):
        return f"Name: {self.name_atr}, Level: {self.level_atr}, HP: {self.hp_atr}, MP: {self.mana_atr}"

    def is_alive(self):
        return self.hp_atr > 0

entity = Character("Entity 1", 99, 1, 999)
print(entity.get_info())

class Player(Character):
    def __init__(self, name, level, hp, mana, str):
        super().__init__(name, level, hp, mana)
        self.str_atr = str
