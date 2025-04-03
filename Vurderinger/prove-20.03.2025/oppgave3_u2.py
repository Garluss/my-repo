import csv
import sys, os
import matplotlib.pyplot as plt

filnavn = fr"{os.path.dirname(sys.argv[0])}/sikkerheit_utf8.csv"

with open(filnavn, encoding="utf-8") as fil:
    innhold = csv.reader(fil,delimiter=";")
    overskrifter = next(innhold)

    angrepstype = []
    for i in innhold:
        angrepstype.append(i[13])
    
    antall = {}
    for i in angrepstype:
        if i not in antall:
            antall[i] = 1
        else:
            antall[i] += 1
    
    sum = 0
    for i in antall:
        sum = sum + antall[i]
    
    print(f"DDos utgjør prosentandel: {antall["DDoS"]/sum*100}%")

    #oppdeling
    typer = []
    telling = []
    for i in antall:
        typer.append(i)
        telling.append(antall[i])



fig, ax = plt.subplots()

pie_colors = ['tab:red', 'tab:blue', 'tab:orange']

ax.pie(telling,labels=typer,colors=pie_colors,autopct='%1.1f%%')
ax.set_title('Fordelingen av angrepsmetoder (vist i prosentandel)')

plt.show()