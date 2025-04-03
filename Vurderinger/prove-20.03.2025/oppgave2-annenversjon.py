import tkinter as tk
from tkinter import font

temperatur = 20.0

def c_opp():
    global temperatur
    temperatur += 0.5
    temp.configure(text=f"Temperatur: \n {temperatur} °C")

def c_ned():
    global temperatur
    temperatur += -0.5
    temp.configure(text=f"Temperatur: \n {temperatur} °C")

def end():
    global startet
    tekst.configure(text="")
    startet = False

startet = False
def c_sett():
    global startet
    if startet == True:
        return
    startet = True
    global temperatur
    tekst.configure(text=f"Temperatur satt til {temperatur} °C")
    root.after(500,lambda: tekst.configure(text=""))
    root.after(1000,lambda: tekst.configure(text=f"Temperatur satt til {temperatur} °C"))
    root.after(1500,end) # Passer på at tekst-boksen ikke blinker for voldsomt når man klikker gjentatte ganger
    # Legger til blinke-funksjon for å legge vekt på den viste teksten, altså endringer i temperatur

root = tk.Tk()

defaultfont = font.nametofont("TkDefaultFont")
defaultfont.configure(size=15)

bigfont = font.Font(size=20)

tk.Button(root,text="Av/På",height=12,width=6).grid(row=0,column=0,rowspan=3,pady=10,padx=10)

ramme1 = tk.Frame(root)
ramme1.configure(borderwidth=1,relief="flat",background="black")
ramme1.grid(row=1,column=1,pady=10,padx=10)

temp = tk.Label(ramme1, text=f"Temperatur: \n {temperatur} °C",font=bigfont,width=12,height=3)
temp.grid(row=1,column=1)

sett = tk.Button(root, text="Sett",height=5,width=6,command=c_sett).grid(row=1,column=2,pady=10,padx=10)
opp = tk.Button(root,text="↑",height=2,width=6,command=c_opp).grid(column=2,row=0,pady=10,padx=10)
ned = tk.Button(root,text="↓",height=2,width=6,command=c_ned).grid(column=2,row=2,pady=10,padx=10)

ramme2 = tk.Frame(root)
ramme2.configure(borderwidth=1,relief="sunken",background="black")
ramme2.grid(column=0,row=3,columnspan=3,pady=10,padx=10)

tekst = tk.Label(ramme2,text=f"",width=35)
tekst.grid(column=0,row=3,columnspan=3)

root.mainloop()