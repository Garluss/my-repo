import csv
import matplotlib.pyplot as plt

menn = {}
kvinner = {}


filnavn = "Lonn_2015-2020.csv"
with open(filnavn, encoding="utf-8") as fil:
    innhold = csv.reader(fil, delimiter="\t")

    overskrifter = next(innhold)

    for rad in innhold:
        if rad[2] == "Menn":
            menn[rad[4]] = rad[5]
        else:
            kvinner[rad[4]] = rad[5]

    