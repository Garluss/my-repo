import random as rd

def rolld(sides):
    if sides == 1:
        return 1
    elif sides < 1:
        return False
    else:
        return rd.randint(1,sides)

class Model:
    def __init__(self,tough=3,save=4,invul=7,wounds=1,fnp=7):
        self.tough = tough
        self.save = save
        self.invulsave = invul
        self.wounds = wounds
        self.feelnopain = fnp
    def atkd(self,atks=1,s=4,str=3,ap=0,dmg=1):
        for i in range(atks):
            result = rolld(6)
            if result >= s:
                print(f"Hit with {result}")
                if str >= 2*self.tough:
                    roll = 2
                elif str > self.tough:
                    roll = 3
                elif str == self.tough:
                    roll = 4
                elif 2*str <= self.tough:
                    roll = 6
                elif str < self.tough:
                    roll = 5
                
                result = rolld(6)
                print(f"Roll to make to wound: {roll}")
                if result < roll:
                    print(f"Failed to wound with {result}")
                    continue
                print(f"Wounded with {result}")
                
                roll = self.save - ap
                result = rolld(6)
                print(f"Roll to make to save: {roll}")
                if self.invulsave < roll:
                    if result >= self.invulsave:
                        print(f"Saved with {result} (invul save)")
                        continue
                else:
                    if result >= roll:
                        print(f"Saved with {result} (armour save)")
                        continue
                print(f"Failed to save with {result}")
                
                if self.feelnopain < 7:
                    neg = 0
                    for i in range(dmg):
                        result = rolld(6)
                        if result >= self.feelnopain:
                            print(f"Rolled {result}, negated 1 damage with Feel-No-Pain")
                            neg += 1
                    dmg = dmg - neg
                    print(f"Negated {neg} damage with Feel-No-Pain")
                
                self.wounds = self.wounds - dmg
                if self.wounds <= 0:
                    print("Defender dead")
                    exit()
            print("Attack missed")
            print(f"Remaining wounds: {self.wounds}")

guardsman = Model(3,4,7,1,7)
voiddragon = Model(11,4,4,12,5)

voiddragon.atkd(16,4,3,0,1)