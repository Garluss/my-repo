def hallo(navn):
    print(f"Hallo {navn}")

def funk(*args:int): #*args viser til et ubestemt antall argumenter (*args eller **kwargs)
    return sum(args)
    print(sum(args)) # return; slutter funksjonen, så denne linjen vil ikke kjøres

funk(1,5)

#En funksjon kan kalle seg selv. Dette kalles rekursjon.
def fak(n):
    if n == 0:
        return 1
    else:
        return n * fak(n-1)

# Kalle funksjonen
print(fak(5))  # Output: 120


#Dokumentasjonsstrenger (docstrings) brukes til å dokumentere funksjoner.
def hei_namn(namn):
    """
    Denne funksjonen skriver ut en hilsen til det gitte navnet.
    
    Parametre:
    namn (str): Navnet som skal hilses.
    """
    print(f"Hei, {namn}!")

# Kalle funksjonen
hei_namn("Ola")


import random as rd

def toTerninger():
  terning1 = rd.randint(1, 6)  
  terning2 = rd.randint(1, 6)
  
  return(terning1, terning2)


mittResultat = toTerninger()

t1, t2 = mittResultat #Pakker ut resultat grunnet to returverdier

print(mittResultat)
print(t1)
print(t2)