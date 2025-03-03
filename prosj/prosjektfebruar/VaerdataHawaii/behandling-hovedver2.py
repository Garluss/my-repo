import csv
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import datetime as dt
import mplcursors

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
                if y < 4:
                    behandlet[i[0]].append((float(i[y])-32)*5/9)
                else:
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
plt.xlabel("Antall dager fra 1940 15. mai (1940 - 2025)")
plt.ylabel("Gjennomsnittstemperatur i celsius (fra fahrenheit)")
plt.xlim(0,500)
plt.ylim(15,35)
plt.colorbar()
cursor = mplcursors.cursor(hover=True)

def text_display(sel):
    date = list(behandlet)[sel.index]
    value = round(ypoints[sel.index],1)
    sel.annotation.set_text(f"Dato: {date}, Temp.: {value} C")
cursor.connect("add", text_display)

text = plt.figtext(0.15,0.05,"test")


slider_color = 'White'
 
# Setter posisjon av akse og glider
axis_position = plt.axes([0.2, 0.1, 0.65, 0.03],facecolor = slider_color)
slider_position = Slider(axis_position, 'Pos', 0.1, 30500.0)
 
def todate(pos,size):
   base = dt.date(1940,5,14)
   base = base + dt.timedelta(pos)
   size = base + dt.timedelta(size)
   string = str(base) + " - " + str(size)
   return string

def update(val):
    pos = slider_position.val
    size = 500
    text.set_text("Viser: " + todate(pos,size))
    Axis.axis([pos, pos+size, 15, 35])
    Plot.canvas.draw_idle()
text.set_text("Viser: " + todate(0,500))
 
slider_position.on_changed(update)

plt.show()