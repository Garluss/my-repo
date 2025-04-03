import csv
import sys, os
import matplotlib.pyplot as plt

filnavn = fr"{os.path.dirname(sys.argv[0])}/sikkerheit_utf8.csv"

def sorter(x):
    return fordeling[x]

with open(filnavn, encoding="utf-8") as fil:
    innhold = csv.reader(fil,delimiter=";")
    overskrifter = next(innhold)

    informasjon = []
    for i in innhold:
        informasjon.append(i[18])
    
    fordeling = {}
    fordeling["Macintosh"] = 0
    fordeling["Windows"] = 0
    fordeling["Annet"] = 0
    for i in informasjon:
        if "Macintosh" in i:
            fordeling["Macintosh"] += 1
        elif "Windows" in i:
            fordeling["Windows"] += 1
        else:
            fordeling["Annet"] += 1
    
    sortert = sorted(fordeling,key=sorter,reverse=True)

    var = sortert[0]
    if var == "Annet":
        var = sortert[1] 
        #Dette passer på at kun alternativene 'Windows' og 'Macintosh' er med i drøftelsen om hvem som er størst, slik som oppgaven spør etter.
        #Dette er egentlig ikke nødvendig i dette tilfellet siden 'Windows' er størst, men for generaliseringsgrunner gjør jeg det alikevel.
    print(f"Operativsystemet {var} blir angrepet oftest.")

    typer = []
    telling = []
    for i in fordeling:
        typer.append(i)
        telling.append(fordeling[i])

fig, ax = plt.subplots()

pie_colors = ['tab:red', 'tab:blue', 'tab:orange']

ax.pie(telling,labels=typer,colors=pie_colors,autopct='%1.1f%%')
ax.set_title('Fordelingen av angripte operativsystem (vist i prosentandel)')

plt.show()