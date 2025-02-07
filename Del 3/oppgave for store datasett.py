import json

from matplotlib import pyplot as plt

filnavn = "05.json"

with open(filnavn,encoding="utf-8") as fil:
    innhold = json.load(fil)
    startstasjoner = {}
    for i in innhold:
        if i["start_station_name"] not in startstasjoner:
            startstasjoner[i["start_station_name"]] = 1
        else:
            startstasjoner[i["start_station_name"]] += 1


#Litt sånn shakey her, kunne vært bedre
def sorter_med_denne(stasjon):
    return startstasjoner[stasjon]

#Mulig å lage egen funksjon og ikke bruke sorted
liste = sorted(startstasjoner,key=sorter_med_denne,reverse=True)
sortert = {}
t = 0
for i in liste:
    if t < 5:
        sortert[i] = startstasjoner[i]
    t = t + 1

navn = sortert.keys()
verdier = sortert.values()

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(navn, verdier)
plt.show()