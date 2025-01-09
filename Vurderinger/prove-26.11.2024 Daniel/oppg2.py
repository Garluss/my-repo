import random
from datetime import datetime, timedelta
class Bil():
    def __init__(self, bilnummer, modell="", farge=""):
        self.bilnummer = bilnummer
        self.modell = modell
        self.farge = farge
        print(f"Opprettet {self.farge} {self.modell}, bilnummer: {self.bilnummer}")
    def get_bilnummer(self):
        return self.bilnummer
    def get_modell(self):
        return self.modell
    def get_farge(self):
        return self.farge

class Annet(Bil):
    def __init__(self, bilnummer, type):
        self.bilnummer = bilnummer
        self.type = type
        print(f"Opprettet {self.type}, bilnummer: {self.bilnummer}")
    def get_type(self):
        return self.type

class PHus():
    def __init__(self, maks_plasser, rate, rate_annet):
        self.maks_plasser = maks_plasser
        self.rate = rate
        self.rate_annet = rate_annet
        self.plasser = 0
        self.biler = {}
        print(f"Opprettet parkeringshus med {self.maks_plasser} plasser, og en pris på {self.rate} kr per minutt ({self.rate_annet} kr/min. for andre fartøy).")
        print("")
    def gen_regist(self):
        reg = ""
        for i in range(5):
            num = random.randint(1,9)
            reg = reg + str(num)
        return reg
    def innkjøring(self, bil, tid):
        if self.plasser >= self.maks_plasser:
            print("Fullt hus.")
            return
        if len(self.biler) > 0:
            while True:
                reg = self.gen_regist()
                if reg not in self.biler:
                    break
        reg = self.gen_regist()
        liste = []
        liste.append(tid)
        liste.append(bil)
        if bil.__class__.__name__ == "Bil":
            print(f"{bil.get_farge().capitalize()} {bil.get_modell()} med bilnummer {bil.get_bilnummer()} kjørte inn. {tid}.")
            print(f"Registrert som {reg}.")
        else:
            print(f"{bil.get_type().capitalize()} med bilnummer {bil.get_bilnummer()} kjørte inn {tid}.")
            print(f"Registrert som {reg}.")
        self.biler[reg] = liste

        self.plasser += 1
        print(f"Antall ledige plasser: {self.maks_plasser - self.plasser}.")
        print("")
    def utkjøring(self, bil, tid):
        for i in self.biler:
            if self.biler[i][1] == bil:
                t1 = self.biler[i][0]
                t2 = tid - t1
                min = t2.seconds // 60
                if bil.__class__.__name__ == "Bil":
                    res = min * self.rate
                else:
                    res = min * self.rate_annet
                print(f"Bil {i} forlot p-hus {tid}.")
                print(f"Parkeringstid på {min} minutt, med avgift {float(res)} kr.")
                self.biler.pop(i)
        
                self.plasser -= 1
                print(f"Antall ledige plasser: {self.maks_plasser - self.plasser}.")
                print("")
                break
    def vis_biler_med_farge(self, farge):
        print(f"Parkerte biler som er {farge}:")
        a = 0
        for i in self.biler:
            bil = bil = self.biler[i][1]
            if bil.__class__.__name__ == "Bil":
                if bil.get_farge() == farge.lower():
                    print(f"  {bil.get_bilnummer()} {bil.get_modell()} (reg.num. {i}).")
                    a += 1
        if a == 0:
            print(f"Ingen biler med farge {farge} funnet.")
        print("")


bil1 = Bil("JD88188","Volvo","svart")
bil2 = Annet("EL11342","lastebil")
phus = PHus(20,1.5,3)

tid = datetime(2024,9,14,16,44)
phus.innkjøring(bil1, tid)

tid = datetime(2024,9,14,16,54)
phus.innkjøring(bil2, tid)

phus.vis_biler_med_farge("svart")

tid = datetime(2024, 9, 14, 17, 22)
phus.utkjøring(bil1, tid)

tid = datetime(2024,9,14,18,41)
phus.utkjøring(bil2, tid)