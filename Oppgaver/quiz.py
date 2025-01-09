import random
sporsmalOrdbok = {
    "Hva er hovedstaten i Norge?":"Oslo",
    "Hva er nabolandene til Norge? (Separer svar med mellomrom)":["Sverige","Russland","Finland"],
    "Hva er Norges befolkning i mil.? (2022)":5.5,
    "Hva er hovedstaten i Kanada?":"Ottowa",
    "Hva er nabolandet til Kanada?":"USA",
    "Hva er Kanadas befolkning i mil.? (2022)":38.9,
    "Hva er hovedstaten i Malaysia?":"Kuala Lumpur",
    "Hva er nabolandene til Malaysia?":["Thailand","Brunei","Singapore","Indonesia"],
    "Hva er Malaysias befolkning i mil.? (2022)":33.9
    }
sporsmal = []
brukteSporsmal = []
for x in sporsmalOrdbok:
    sporsmal.append(x)

poeng = 0
poeng = float(poeng)
poengMax = 0
poengMax = float(poengMax)
antallSporsmal = 9
if antallSporsmal > len(sporsmal):
    print("Ikke nok tilgjengelige spørsmål!")
    exit()
for i in range(antallSporsmal):
    while True:
        s = random.choice(sporsmal)
        if s not in brukteSporsmal:
            brukteSporsmal.append(s)
            break
    print(s)
    sSvar = input("Ditt svar: ")
    try:
        if float(sSvar) == float(sporsmalOrdbok[s]):
            print("Perfekt svar! Du får 1 poeng.")
            poeng += 1
        elif float(sSvar) <= float(sporsmalOrdbok[s]*1.1) and float(sSvar) >= float(sporsmalOrdbok[s]*0.9):
            print("Ikke helt korrekt, men nærme nok. Du får 0.5 poeng.")
            poeng += 0.5
        else:
            print("FEIL SVAR DIN IDIOT!")
        poengMax += 1
    except ValueError:
        try:
            if type(sporsmalOrdbok[s]) == list:
                sSvar = sSvar.split()
                iSvar = False
                sPoeng = 0
                for y in range(len(sSvar)):
                    for x in range(len(sporsmalOrdbok[s])):
                        if sSvar[y].lower() == sporsmalOrdbok[s][x].lower():
                            sPoeng += 1
                            poeng += 1
                            iSvar = True
                    if iSvar == False:
                        print("FEIL SVAR DIN IDIOT!")
                    poengMax += 1
                print(f"Du har fått {sPoeng} av {len(sporsmalOrdbok[s])} mulige poeng på dette spørsmålet!")

            else:
                if sSvar.lower() == sporsmalOrdbok[s].lower():
                    print("Riktig svar! Du får 1 poeng.")
                    poeng += 1
                else:
                    print("FEIL SVAR DIN IDIOT!")
                poengMax += 1
        except AttributeError:
            print("Skriv inn en passende objekttype!")
    print("")

print(f"Du fikk {poeng} av {poengMax} mulige poeng")
if poeng == poengMax:
    print("Et perfekt resultat!")