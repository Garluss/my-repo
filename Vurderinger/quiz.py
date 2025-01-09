import random

Norge = {"Hva er hovedstaten i Norge?":"Oslo","Hva er innbyggertallet i Norge?":"5000000","Naboland til Norge?":"SverigeFinlandRussland"}
Kanada = {"Hva er hovedstaten i Kanada":"Ottowa","Hva er innbyggertallet i Kanada?":"39000000","Naboland til Kanada?":"USADanmark"}
nS =[]
nV = []
kS = []
kV = []
for x in Norge:
    nS.append(x)
    nV.append(Norge[x])
for x in Kanada:
    kS.append(x)
    kV.append(Kanada[x])

poeng = 0
for i in range(3):
    land = random.randint(0,5)
    if land > 2:
        land = land-3
        print(kS[land])
        svar = input("Ditt svar: ")
        if svar.lower() in kV[land].lower():
            print("Du fikk rett")
            poeng += 1
        else:
            print(f"Riktig svar var {kV[land]}")
    else:
        print(nS[land])
        svar = input("Ditt svar: ")
        if svar.lower() in nV[land].lower():
            print("Du fikk rett")
            poeng += 1
        else:
            print(f"Riktig svar var {nV[land]}")
print(f"Du fikk {poeng} av 3 mulige poeng")