import csv
import os, sys
import timeit

def code():
    filnavn = fr"{os.path.dirname(sys.argv[0])}/Electric_Vehicle_Population_Data.csv"

    with open(filnavn,encoding="utf-8") as dt:
        ark = csv.reader(dt)
        overskrifter = next(ark)
        liste = []
        for i in ark:
            liste.append(i)
        produsenter = {} #finner topp 3 produsenter
        for i in liste:
            if i[6] in produsenter:
                produsenter[i[6]] += 1
            else:
                produsenter[i[6]] = 1
        top = []
        for i in range(3): #antall top-produsenter som ønskes
            top.append(sorted(produsenter,key=lambda x: produsenter[x],reverse=True)[i])
        print(top)

antall = 10
print(f"Tid for å kjøre {antall} ganger: {timeit.timeit(code,number=antall)}s")