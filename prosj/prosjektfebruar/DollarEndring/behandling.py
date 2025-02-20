import csv
import matplotlib.pyplot as plt

filnavn = "dataset_dollar.csv"
with open(filnavn,mode="r") as fil:
    innhold = csv.reader(fil,delimiter=",")
    overskrift = next(innhold)

    behandlet = {}
    t = 0
    for i in innhold:
        behandlet[t] = []
        behandlet[t] = i[1:6]
        behandlet[t][4] = behandlet[t][4].replace("%","")
        t += 1
    print(behandlet[0])

    
xpoints = []
ypoints = []

plt.plot(xpoints,ypoints)
plt.title("Temperatur i Hawaii (Honolulu Lufthavn)")
plt.xlabel("Antall dager fra 1940 14. mai (1940 - 2025)")
plt.ylabel("Temperatur målt i fahrenheit")

plt.show()