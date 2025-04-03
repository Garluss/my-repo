import csv
import sys, os

filnavn = fr"{os.path.dirname(sys.argv[0])}/sikkerheit_utf8.csv"

def sorter(x):
    return antall[x]

with open(filnavn, encoding="utf-8") as fil:
    innhold = csv.reader(fil,delimiter=";")
    overskrifter = next(innhold)

    protokoller = []
    for i in innhold:
        protokoller.append(i[5])
    
    antall = {}
    for i in protokoller:
        if i not in antall:
            antall[i] = 1
        else:
            antall[i] += 1
    
    sortert = sorted(antall,key=sorter,reverse=True)
    
    print("De tre mest brukte protokollene er: (i synkende rekkefølge)")
    for i in range(3):
        print(f"Nr. {i+1}: {sortert[i]}")