import csv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

filnavn = "data.csv"
with open(filnavn,mode="r") as fil:
    innhold = csv.reader(fil,delimiter=",")
    stasjon = next(innhold)
    overskrift = next(innhold)

    behandlet = {}
    previous = next(innhold)
    for i in innhold:
        behandlet[i[0]] = []
        for y in range(1,4):
            try:
                behandlet[i[0]].append(int(i[y]))
            except:
                behandlet[i[0]].append(None)
xpoints = []
ypoints = []
t = 0
for i in behandlet:
    if behandlet[i][1] != None and behandlet[i][2] != None:
        value = (behandlet[i][1]+behandlet[i][2])/2
    else:
        value = None
    xpoints.append(t)
    ypoints.append(value)
    t += 1

Plot, Axis = plt.subplots()
plt.subplots_adjust(bottom=0.25)

plt.scatter(xpoints,ypoints,c=ypoints,cmap="viridis",s=3)
plt.title("Temperatur i Hawaii (Honolulu Lufthavn)")
plt.xlabel("Antall dager fra 1940 14. mai (1940 - 2025)")
plt.ylabel("Temperatur målt i fahrenheit")
plt.xlim(0,500)
plt.ylim(60,90)
plt.colorbar()

slider_color = 'White'
 
# Set the axis and slider position in the plot
axis_position = plt.axes([0.2, 0.1, 0.65, 0.03],facecolor = slider_color)
slider_position = Slider(axis_position, 'Pos', 0.1, 30500.0)
 
def update(val):
    pos = slider_position.val
    Axis.axis([pos, pos+500, 60, 90])
    Plot.canvas.draw_idle()
 
slider_position.on_changed(update)

plt.show()