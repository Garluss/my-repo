'''
tall = []
for i in range(1,101):
    tall.append(i)

sjekk = input("Skriv inn tall: ")
sjekk = int(sjekk)

def delelig(liste,sjekk=2):
    ferdig = []
    for i in liste:
        if int(i) % int(sjekk) == 0:
            ferdig.append(i)
    return ferdig

print("Søker med tallet " + str(sjekk))
for i in delelig(tall,sjekk):
    print(i)
'''

import datetime
aarN = datetime.datetime.now()
aarN = aarN.strftime("%y")


nummer = "02069833478"

#sjekker om personnummeret kun inneholder tall
try:
    int(nummer)
except ValueError:
    print("Må kun være sifre!")
    #continue
    exit()

#sjekker lengden på personnummeret er gydlig
if len(nummer) != 11:
    print("Ikke riktig lengde. Må være 11 sifre.")
    exit()

#info fra personnummer
dag = nummer[0:2]
maaned = nummer[2:4]
aar = nummer[4:6]
pers = nummer[6:11]

#gir en månedsverdi til de ulike tallene ( ver. 1 )
def maaned1(tall):
    match tall:
        case "01": return "januar"
        case "02": return "februar"
        case "03": return "mars"
        case "04": return "april"
        case "05": return "mai"
        case "06": return "juni"
        case "07": return "juli"
        case "08": return "august"
        case "09": return "september"
        case "10": return "oktober"
        case "11": return "november"
        case "12": return "desember"
        case _: return "ukjent"

#gir en månedsverdi til de ulike tallene ( ver 2 )
def maaned2(tall):
    maanader = {
        "01":"januar",
        "02":"februar",
        "03":"mars",
        "04":"april",
        "05":"mai",
        "06":"juni",
        "07":"juli",
        "08":"august",
        "09":"september",
        "10":"oktober",
        "11":"november",
        "12":"desember"
    }
    if tall in maanader:
        return maanader[tall]

#fjerner null-en foran dato (dag) hvis den har en null der
if dag[0] == "0":
    dag = dag.replace("0","")

#sjekker om persononen er født i år, på 1900-tallet eller 2000-tallet
if aar == aarN:
    print("Ikke gyldig årstall.")
    exit()
elif aar > aarN:
    aar = "19" + aar
elif aar < aarN:
    aar = "20" + aar

#sjekker om personen er mann eller kvinne ved å finne ut om personnummeret er partall eller oddetall
if int(nummer) % 2 == 0:
    kjonn = "kvinne"
else:
    kjonn = "mann"

#printer ut den endelige formateringen av fødselsdatoen
print(f"Fødselsdatoen er {dag}. {maaned2(maaned)} {aar}, person {pers} ({kjonn})")