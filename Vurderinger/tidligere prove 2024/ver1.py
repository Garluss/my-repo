import csv
import sys, os
import matplotlib.pyplot as plt

filnavn = fr"{os.path.dirname(sys.argv[0])}/run_ww_2020_w-PROVE.csv"
with open(filnavn, encoding="utf-8") as fil:
    innhold = csv.reader(fil,delimiter=",")
    overskrifter = next(innhold)

    aldre = []
    for i in innhold:
        aldre.append(i[6])

    typer_alderstrinn = []
    for i in aldre:
        if i in typer_alderstrinn:
            continue
        else:
            typer_alderstrinn.append(i)

    antall = []
    for i in typer_alderstrinn:
        tall = aldre.count(i)
        print(f"I alderskategorien {i} er det {tall} utøvarar.")
        antall.append(tall)

fig, ax = plt.subplots()

bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

ax.bar(typer_alderstrinn, antall, label=typer_alderstrinn, color=bar_colors)

ax.set_ylabel('Antall idrettsutøvarar')
ax.set_title('Idrettsutøvarar i ulike alderskategoriar')
ax.legend(title='Farge')

plt.show()