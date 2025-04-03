def karakter(poengsum:int)->str:
    if poengsum < 50:
        return("Ikke bestått")
    elif 50 < poengsum < 69:
        return("Bestått")
    elif 70 < poengsum < 89:
        return("Godt bestått")
    elif 90 < poengsum < 100:
        return("Meget godt bestått")
    else:
        return("Ikke gyldig poengsum!")

print(karakter(30)) #korrekt
print(karakter(65)) #korrekt
print(karakter(82)) #korrekt

print(karakter(0)) #korrekt
print(karakter(50)) #feil
print(karakter(69)) #feil
print(karakter(70)) #feil
print(karakter(89)) #feil
print(karakter(90)) #feil
print(karakter(100)) #feil
print(karakter(-1)) #feil

def karakter_ordnet(poengsum:int)->str:
    if 0 <= poengsum < 50:
        return("Ikke bestått")
    elif 50 <= poengsum <= 69:
        return("Bestått")
    elif 70 <= poengsum <= 89:
        return("Godt bestått")
    elif 90 <= poengsum <= 100:
        return("Meget godt bestått")
    else:
        return("Ikke gyldig poengsum!")