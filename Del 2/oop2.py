#Eksempel på arv, der et rektangel er et spesielt tilfelle av et kvardrat, og dermed arver de fleste av atributtene

#Superklasse av kvadrat
class Rektangel:
    def __init__(self, lengde, bredde):
        """Konstruktør"""
        self.lengde = lengde
        self.bredde = bredde
    
    def areal(self):
        """Metode for beregningen av areal"""
        return self.lengde * self.bredde

#Klassen arver fra kvadratet
#Subklasse av rektangel
class Kvadrat(Rektangel):
    def __init__(self, sidekant):
        #Vi bruker super() for å hente metoder fra superklassen til kvadrat (rektangel)
        super().__init__(sidekant, sidekant)


#Nytt eksempel der subklassen har mer informasjon enn superklassen
class Billett():
    def __init__(self):
        self.mva = 0.12
        self.pris = 20

    def beregnPris(self):
        return self.pris + (self.pris * self.mva)

#Barnebilletten skal ha en rabatt på 50% i forhold til den normale billetten
class Barnebillett(Billett):
    def  __init__(self):
        super().__init__()
        self.rabatt = 0.5
    #Dette eksempelet kompless overstyrer superklassens metode
    def beregnPris(self):
        rabattpris = self.pris * self.rabatt
        return rabattpris + (rabattpris * self.mva)
    #Dette eksempelet baserer seg på sluttproduktet hvis superklassen hadde kjørt det og deretter legger til rabatt
    def beregnPrisAlternativ(self):
        return super().beregnPris() * self.rabatt
