import random as rd


class Model:
    def __init__(self, m, t, sv, w, ld, oc, ab, invul, fnp):
        self.m = m
        self.t = t
        self.sv = sv
        self.w = w
        self.ld = ld
        self.oc = oc
        self.ab = ab #abilities, any
        self.invul = invul #tuple, can for example be: (5, "RANGED") or (4, "ANY")
        self.fnp = fnp #can be None or int
    def take_damage(self, amt, ap, type, d): #type can be "RANGED" or "MELEE"
        for i in range(amt):
            n = rd.random(1,6)
            if self.invul != None and self.invul < self.sv-ap and type == self.invul[1] or type == "MELEE" and self.invul == "ANY":
                sv = self.invul
            else:
                sv = self.sv
            if n < sv:
                if self.fnp != None:
                    for i in range(d):
                        n = rd.random(1,6)
                        if n >= self.fnp:
                            continue
                        self.w = self.w - 1
                else:
                    self.w = self.w - d

class Weapon:
    def __init__(self, range, a, skill, s, ap, d, ab, type):
        self.range = range
        self.a = a #int or f"{str(int)}D{str(int)}+{str(int)}"
        self.skill = skill
        self.s = s
        self.ap = ap #0 or a negative int
        self.d = d
        self.ab = ab #abilities
        self.type = type #"RANGED" or "MELEE"
    def attack(self, target):
        if type(self.a) == str:
            if self.a[0] == "D" and len(self.a) == 2:
                attacks = rd.random(1,6)
            elif self.a[0] == "D" and len(self.a) > 2:
                attacks = rd.random(1,6)
                attacks += self.a[3]
            elif self.a[0] != "D" and len(self.a) == 3:
                attacks = 0
                for i in range(self.a[1]):
                    n = rd.random(1,6)
                    attacks = attacks + n
            elif self.a[0] != "D" and len(self.a) > 3:
                attacks = 0
                for i in range(self.a[1]):
                    n = rd.random(1,6)
                    attacks = attacks + n
                attacks += self.a[4]
            
    
    
            