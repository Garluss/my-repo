import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

def eksploder():
    global status
    if status == 1:
        label.configure(image=bild)
        knapp.configure(text="Restorer")
    elif status == -1:
        label.configure(image=bilde)
        knapp.configure(text="Eksploder")
    status = status * -1

status = 1

root = tk.Tk()
root.title("Vindu kult")

defaultfont = font.nametofont("TkDefaultFont")
defaultfont.configure(family="Comic Sans MS", size=20)

bild = Image.open("funny2.jpg")
bild = bild.resize((400,200))
bild = ImageTk.PhotoImage(bild)

bilde = Image.open("funny.jpg")
bilde = bilde.resize((400,200))
bilde = ImageTk.PhotoImage(bilde)
label = tk.Label(root, image=bilde)

label.grid(row=0,column=0,padx=5,pady=5)

ramme = tk.Frame(root, padx=10,pady=10)
ramme.grid(row=0,column=1,padx=5,pady=5)

knapp = tk.Button(ramme, text="Eksploder", command=eksploder)
knapp.grid(row=0, column=0)

root.mainloop()