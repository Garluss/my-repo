import math as m

liste = []

ordbok = { "navn":"per", "etternavn":"bjørnson" }

print(type(liste))
print(type(ordbok))



class Planet:
    """
    Klasse for planet-objekter

    Parametre:
        navn (str): Planetens navn
        solavstand (float): Avstand fra sola målt i en eller annen verdi (det er ikke så viktig)
        radius = 23 (float): Radien? Radius? Bare sett inn et tall du liker. Den normale verdien er 23 så du får ta noe lignende i stoerrelse?
    """
    def __init__(self, navn, solavstand, radius = 23): #Vi kan sette standardverdier i atributtene til klasser ved å skrive "=" og så verdien bak atributten
        """
        Konstruktoer
        """
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
    
    def volum(self):
        """
        Metode som gir det volumet av planeten i hvilken måleenhet du valgte å bruke på radius
        """
        return (4/3) * m.pi * self.radius**3
    
    def visInfo(self):
        print(f"Planeten sitt navn: {self.navn}, solavstand: {self.solavstand}, radius: {self.radius}")


burbukos = Planet("Burbukos", 21, 233)
jalaland = Planet("Jala Land", 333, 58008)
default = Planet("sjekk radius-verdien", 221)

print(default.radius)
burbukos.visInfo()

print("hei" in "heipaadeg")