import tkinter as tk
from tkinter import font

root = tk.Tk()

defaultfont = font.nametofont("TkDefaultFont")
defaultfont.configure(family="Comic Sans MS", size=20)

label1 = tk.Label(root, text="Hei")
label1.grid(row=0,column=0, padx=30)

label2 = tk.Label(root,text="Hallo")
label2.grid(row=0,column=1, padx=30)

root.mainloop()