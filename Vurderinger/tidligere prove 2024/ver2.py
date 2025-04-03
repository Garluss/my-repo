import csv
import sys, os
import matplotlib.pyplot as plt
import datetime as dt

def uke(x):
    dato = dt.datetime.strptime(x.replace("-"," "),"%Y %m %d")
    _, w, _ = dato.isocalendar()
    return w


filnavn = fr"{os.path.dirname(sys.argv[0])}/run_ww_2020_w-PROVE.csv"
with open(filnavn, encoding="utf-8") as fil:
    innhold = csv.reader(fil,delimiter=",")
    overskrifter = next(innhold)

    info = []
    for i in innhold:
        info.append((uke(i[1]),i[4]))
    
    uketall = []
    for i in info:
        if i[0] in uketall:
            continue
        else:
            uketall.append(i[0])
    
    print(uketall)
    print(info[:10])