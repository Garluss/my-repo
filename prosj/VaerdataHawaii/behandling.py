import csv
import matplotlib.pyplot as plt

filnavn = "data.csv"
with open(filnavn,mode="r") as fil:
    innhold = csv.reader(fil,delimiter=",")
    stasjon = next(innhold)
    overskrift = next(innhold)

    behandlet = {}
    previous = []
    ## Ta noe for de første verdiene
    for i in innhold:
        behandlet[i[0]] = []
        behandlet[i[0]].append(int(i[1].replace("",previous[0])))
        behandlet[i[0]].append(int(i[2].replace("",previous[1])))
        behandlet[i[0]].append(int(i[3].replace("",previous[2])))
        previous.extends(behandlet[i])

    
xpoints = []
ypoints = []
for i in behandlet:
    xpoints.append(i)
    ypoints.append(behandlet[i][0])

plt.plot(xpoints,ypoints)
plt.show()