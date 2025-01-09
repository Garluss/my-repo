import random
import time


class Karakter:
    def __init__(self, navn = "NPC", helse = 3.0, angrep = 1.0, beskyttelse = 0.0, parr = False):
        self.navn = navn
        self.helse = helse
        self.angrep = angrep
        self.beskyttelse = beskyttelse
        self.parr = parr
    
    def angrepet(self, x):
        if self.parr == True:
            self.helse = self.helse - (x  - x*0.05*self.beskyttelse) * 0.5
            self.parr = False
        else:
            self.helse = self.helse - (x - x*0.05*self.beskyttelse)
    
    def parry(self):
        self.parr = True

print("Velkommen eventyrer. Hva er ditt storslotte navn? ")
spiller = Karakter(helse=5.0)
spiller.navn = str(input())
print("")
print(f"Ditt navn er {spiller.navn}, velkommen.")

#karakterer
padde = Karakter("Gamle Padde",20.0,5.0,3.0)



def kommando(valg):
    while True:
        komm = input("Valg (hjelp: (h)): ").lower().strip()
        if komm == "h":
            print("Mulige kommandoer er: a (attributter), h (hjelp), v (valg)")
        elif komm == "a":
            print(f"Navn: {spiller.navn}, helse: {spiller.helse}, angrep: {spiller.angrep}, beskyttelse: {spiller.beskyttelse}")
        elif komm == "v":
            print(f"Mulige valg er: {valg}")
        elif komm in valg:
            print("")
            return komm
        else:
            print("Ikke en gyldig kommando")

def kamp(fiende):
    while True:
        komm = input("Valg (hjelp: (h)): ").lower().strip()
        if komm == "h":
            print("Mulige kommandoer er: a (attributter), h (hjelp), atk (angrip), par (parry), s (sjekk)")
        elif komm == "a":
            print(f"Navn: {spiller.navn}, helse: {spiller.helse}, angrep: {spiller.angrep}, beskyttelse: {spiller.beskyttelse}")
        elif komm == "atk":
            fiende.angrepet(spiller.angrep)
            print(f"Du angriper {fiende.navn} for {spiller.angrep}!")
            break
        elif komm == "par":
            spiller.parr = True
            print("Du klargjør våpenet ditt.")
            break
        elif komm == "s":
            print(f"Navn: {fiende.navn}, helse: {fiende.helse}, angrep: {fiende.angrep}, beskyttelse: {fiende.beskyttelse}")
            time.sleep(3)
            break
        else:
            print("Ikke en gyldig kommando")

def kampstart(fiende):
    print("! Kamp !")
    for x in range(30):
        spiller.parr = False
        kamp(fiende)
        if fiende.helse <= 0:
            print("Fienden er død.")
        time.sleep(1)
        fiende.parr = False
        fvalg = random.randint(1,2)
        if fvalg == 1:
            spiller.angrepet(fiende.angrep)
            print(f"{fiende.navn} angriper deg for {fiende.angrep} skade!")
            time.sleep(1)
            print(f"Resterende helse er: {spiller.helse}")
            if spiller.helse <= 0:
                print("Du er død.")
                exit()
        else:
            fiende.parr = True
            print("Fienden klargjør våpenet sitt.")
            time.sleep(1)


time.sleep(1)
print("Du er i en tett skog.")
time.sleep(1)
print("Du vet ikke helt hvordan du kom hit.")
time.sleep(2)
print("Det er tid for å handle.")

naavalg = ["venstre", "høyre"]
valg = kommando(naavalg)
print(valg)
if valg == "venstre":
    print("Du tråkker videre inn i skogen, gjennom en gjørmete sti.")
    time.sleep(1)
    print("Du ser foran deg en skrøpelig gammel padde.")
    time.sleep(2)
    print("Det er tid for å handle.")
    naavalg = ["angrip", "snakk"]
    valg = kommando(naavalg)
    print(valg)
    if valg == "angrip":
        kampstart(padde)
elif valg == "høyre":
    print("Du går på en ryddig grussti.")


