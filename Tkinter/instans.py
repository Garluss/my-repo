import tkinter as tk
import random as rd

class Dings():
    def __init__(self):
        self.navn = rd.choice(["Jens","Truls","Per","Ane","Lisa","Rogn","Kulf","Propp","Snipp","Snapp","Klapp","Persille","Bustad","Kruls","Knoll","Probert","Snobert"])
        self.farge = rd.choice(["Brun","Gul","Svart","Regnbue"])

babies = []
def rep():
    inst = Dings()
    babies.append(inst)
def slakt():
    try:
        n = rd.randint(0,len(babies)-1)
        bn = babies[n].navn
        bf = babies[n].farge
        babies.pop(n)
        print(f"Slaktet {bn} ({bf})")
    except:
        print("No babies to slakte")


root = tk.Tk()

root.title("Egypt-simulator")

knapp = tk.Button(root,text="Reproduser.",command=rep,padx=5,pady=5).pack()
vis = tk.Button(root,text="vis",command=lambda: [print(f"{i.navn} ({i.farge})") for i in babies],padx=120,pady=20).pack()
sløy = tk.Button(root,text="Slakt",command=slakt).pack()

root.mainloop()