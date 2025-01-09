import math
import random
import time

print("WORLD START")
print("")

class Entity():
    def __init__(self, name, level, str, hp, defense):
        self.name = name
        self.level = level
        self.str = str
        self.hp = hp
        self.defense = defense
    
    def get_info(self):
        return f"Name: {self.name} \nLevel: {self.level} \nSTR: {self.str}, HP: {self.hp}"
    
    def attack(self, target):
        damage = self.str + self.str * (random.randint(1,20)/100)
        target.take_damage(damage)
        return damage
    
    def take_damage(self, damage):
        if self.defense < 0:
            self.hp = self.hp - damage
        else:
            formula = damage/(self.defense+1)

            self.hp = self.hp - (formula + formula * random.randint(-10,10)/100)
            return formula
    
    def is_alive(self):
        return self.hp > 0


class Item():
    def __init__(self, name: str, i_def, i_str, i_hp, i_mp):
        self.name = name
        self.i_def = i_def
        self.i_str = i_str
        self.i_hp = i_hp
        self.i_mp = i_mp
    
    def get_stat(self, stat):
        match stat:
            case "name": return self.name
            case "def": return self.i_def
            case "str": return self.i_str
            case "hp": return self.i_hp
            case "mp":return self.i_mp
            case _: return False

class Player(Entity):
    def __init__(self, name, level, exp, str, hp, mp, atr_str, atr_hp, atr_mp, equipment = [], defense = 0):
        super().__init__(name, level, str, hp, defense)
        self.exp = exp
        self.mp = mp
        self.atr_str = atr_str
        self.atr_hp = atr_hp
        self.atr_mp = atr_mp
        self.equipment = equipment
    
    def level_curve(self):
        return self.level*2
    
    def give_exp(self, amt):
        self.exp = self.exp + amt
        while True:
            if self.exp >= self.level_curve():
                self.exp = self.exp - self.level_curve()
                self.level = self.level + 1
                while True:
                    try:
                        self.level_stat(input("Choose a stat to increase (str, hp, mp):"), 1)
                    except:
                        print("Invalid stat.")
                        continue
                    break
            else:
                break

    def level_stat_rate(self, atr):
        return atr*2

    def level_stat(self, stat:str, levels:int):
        match stat:
            case "str":
                self.atr_str += levels
                for i in range(levels):
                    self.str = self.level_stat_rate(self.str)
            case "hp":
                self.atr_hp += levels
                for i in range(levels):
                    self.hp = self.level_stat_rate(self.hp)
            case "mp":
                self.atr_mp += levels
                for i in range(levels):
                    self.mp = self.level_stat_rate(self.mp)
    
    def get_stat(self, stat):
        match stat:
            case "name": return self.name
            case "level": return self.level
            case "exp": return self.exp
            case "str": return self.str
            case "hp": return self.hp
            case "mp":return self.mp
            case "atr_str": return self.atr_str
            case "atr_hp": return self.atr_hp
            case "atr_mp": return self.atr_mp
            case _: return False

    def get_info(self):
        return f"Name: {self.name} \nLevel: {self.level} \nSTR: {self.str}, HP: {self.hp}, MP: {self.mp}, Defense: {self.defense} \nSTR (atr.): {self.atr_str}, HP (atr.): {self.atr_hp}, MP (atr.): {self.atr_mp}"

    def get_items(self):
        return self.equipment
    
    def showfancy_items(self):
        items = ""
        for i in self.equipment:
            if i != self.equipment[len(self.equipment)-1]:
                items = items + i + ", "
            else:
                items = items + i
        return f"Equipment: \n{items}"

    def equip(self, equipment):
        if len(self.equipment) < 4:
            self.equipment.append(equipment.get_stat("name"))
            self.defense += equipment.get_stat("def")
            self.hp += equipment.get_stat("hp")
            self.mp += equipment.get_stat("mp")
            self.str += equipment.get_stat("str")
        else:
            print("You are already carrying the maximum amount of items.")


# player1.equip(wooden_shield)
# player1.equip(heavy_chestplate)
# print(player1.get_info())

class Map():
    def __init__(self, map={}, size_x=1, size_y=1):
        self.map = map
        self.size_x = size_x
        self.size_y = size_y

    def load_map(self, file_path):
        m = open(file_path, 'r')
        map = m.read()
        m.close()
        t = 0
        map = map.replace('\n','')
        dict = {}
        for i in range(self.size_y):
            list = []
            for j in range(self.size_x):
                list.append(map[t])
                t += 1
            dict[i] = list
        self.map = dict
    
    def get_map_str(self):
        map = self.map
        str = ""
        for i in map:
            for l in map[i]:
                str = str + l
            if i+1 < self.size_y:
                str = str + "\n"
        return str
    
    def get_map_dict(self):
        return self.map
    
    def get_coordinate(self, coordinate_x, coordinate_y):
        map = self.get_map_dict()
        if coordinate_x < 0:
            return "-"
        elif coordinate_y < 0:
            return "-"
        elif coordinate_x > self.size_x-1:
            return "-"
        elif coordinate_y > self.size_y-1:
            return "-"
        else:
            return map[coordinate_y][coordinate_x]
    
    def set_coordinate(self, coordinate_x, coordinate_y, char="O"):
        map = self.map
        map[coordinate_y][coordinate_x] = char
        self.map = map
    
    def render_range(self,x,y,srange=5):
        s = []
        s.append(x-math.floor(srange/2))
        s.append(y-math.floor(srange/2))
        img = ""
        for i in range(srange):
            for j in range(srange):
                img = img + self.get_coordinate(int(s[0]+j),int(s[1]+i))
            if i+1 < srange:
                img = img + "\n"
        return img
    
    def player_pos(self, x, y, range=5, setcursor="", previous="#", prev_x=0, prev_y=0):
        if setcursor != "":
            if prev_x != 0 and prev_y != 0:
                self.set_coordinate(prev_x,prev_y,previous)
            self.set_coordinate(x,y,setcursor)
        return self.render_range(x,y,range)

class Game():
    def __init__(self, playerobj, map, walkable):
        self.player = playerobj
        self.map = map
        self.moving = True
        self.walkable = walkable
    
    def start(self, x, y):
        prev_x = x
        prev_y = y
        previous = self.map.get_coordinate(x,y)
        print(self.map.player_pos(x,y,9,"O"))
        while self.moving == True:
            move = input("Beveg opp, ned, høy, ven: ")
            match move:
                case "opp":
                    if self.map.get_coordinate(x,y-1) in self.walkable:
                        y = y - 1
                case "ned":
                    if self.map.get_coordinate(x,y+1) in self.walkable:
                        y = y + 1
                case "høy":
                    if self.map.get_coordinate(x+1,y) in self.walkable:
                        x = x + 1 
                case "ven":
                    if self.map.get_coordinate(x-1,y) in self.walkable:
                        x = x - 1
                case "info":
                    print(self.player.get_info())
                    continue
                case _:
                    print("Ikke gjenkjent retning. Prøv på nytt.")
            print(self.map.player_pos(x,y,9,"O",previous,prev_x,prev_y))
            if x != prev_x or y != prev_y:
                previous = self.map.get_coordinate(prev_x,prev_y)
            prev_x = x
            prev_y = y

player1 = Player("Player", 1, 0, 1, 3, 5, 1, 1, 1)
wooden_shield = Item("Wooden Shield",1,0,0,0)
heavy_chestplate = Item("Heavy Chestplate", 8, -1, 4, 0)
overworld = Map(0,55,13)
overworld.load_map("D:\SKOLE\Programmer - IT2\Del 2\main.txt")

walkablelist = ["#"]
level1 = Game(player1,overworld,walkablelist)
level1.start(11,3)