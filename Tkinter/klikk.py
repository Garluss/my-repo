import tkinter as tk
from tkinter import font

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Klikker")

        self.klikk = 0

        self.label = tk.Label(self.root, text=self.klikk)
        self.label.pack()

        tk.Button(self.root,text="Klikk meg!",command=self.klikker).pack()

    def klikker(self):
        self.klikk += 1
        self.label.configure(text=self.klikk)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()