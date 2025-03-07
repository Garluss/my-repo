import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bildevisning")
        #self.root.geometry("500x400")

        self.bilder = [
            "funny.jpg",
            "funny2.jpg",
            "goober.png"
        ]

        self.index = 0

        self.bilde = tk.Label(self.root)
        self.bilde.grid(row=0,column=0,padx=5,pady=5)

        self.frame = tk.Frame(self.root)
        self.frame.grid(row=1,column=0,padx=10,pady=10)

        tk.Button(self.frame, text="<", width=2, command=self.forrige_bilde).grid(row=0,column=0,padx=5,pady=5)
        tk.Button(self.frame, text=">", width=2, command=self.neste_bilde).grid(row=0,column=1,padx=5,pady=5)
        self.b = None

        self.vis_bilde()

    def vis_bilde(self):
        self.b = Image.open(self.bilder[self.index])
        self.b = self.b.resize((450,350))
        self.b = ImageTk.PhotoImage(self.b)
        self.bilde.configure(image=self.b)
    
    def neste_bilde(self):
        if self.index < len(self.bilder)-1:
            self.index += 1
        else:
            self.index = 0
        self.vis_bilde()
    
    def forrige_bilde(self):
        if self.index > 0:
            self.index += -1
        else:
            self.index = len(self.bilder)-1
        self.vis_bilde()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()