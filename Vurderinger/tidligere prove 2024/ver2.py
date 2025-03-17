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

    ukenumre = []
    for i in innhold:
        ukenumre.append(uke(i[1]))
    
    uketall = []
    for i in ukenumre:
        if i in uketall:
            continue
        else:
            uketall.append(i)

    antall = []
    for i in uketall:
        tall = ukenumre.count(i)
        antall.append(tall)
    print(antall)

#like mange entries hver uke?

fig, ax = plt.subplots()

bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

ax.bar(uketall, antall, label=uketall, color=bar_colors)

ax.set_ylabel('Antall løp i uke')
ax.set_title('Løp i ulike uker')
ax.legend(title='Farge')

plt.show()