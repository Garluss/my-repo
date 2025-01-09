import random

#Maskinen spiller stein, saks, papir
#1 er saks, 2 er stein 3 er papir

s1vic = 0
s2vic = 0
tie = 0
for i in range(500000):
    s1 = random.randint(1,3)
    s2 = random.randint(1,3)


    if s1 == s2:
        tie += 1
    elif s1 > s2:
        if s2 == 1:
            s2vic += 1
    elif s2 > s1:
        if s1 == 1:
            s1vic += 1

print(f"Spiller 1 vunnet: {s1vic}")
print(f"Spiller 2 vunnet: {s2vic}")
print(f"Uavgjort: {tie}")