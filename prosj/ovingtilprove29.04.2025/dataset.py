import csv
import os, sys

filnavn = fr"{os.path.dirname(sys.argv[0])}/Electric_Vehicle_Population_Data.csv"

with open(filnavn,encoding="utf-8") as dt:
    ark = csv.reader(dt)
    overskrifter = next(ark)
    liste = []
    for i in ark:
        liste.append(i)
    print(liste[0])