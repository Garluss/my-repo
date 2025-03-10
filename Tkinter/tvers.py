import tkinter as tk
from tkinter import font

class App():
    def __init__(self):
        print("Starting...")
        self.root = tk.Tk()
    
        self.boxes = []
        self.letters = []
        self.actual_letters = []

        self.length = 5
        self.width = self.length*60
        self.root.geometry(f"{self.width}x150")
        self.create_boxes(self.length)
        self.create_letters(self.length)

        self.current_letter = None

        self.root.bind("<Motion>",self.drag)

    def create_boxes(self, amt):
        for i in range(amt):
            self.boxes.append(tk.Frame(self.root,bg="red",width=40,height=40))
        t = 0
        for i in self.boxes:
            i.place(x=20+((self.width-20)/self.length)*t,y=10) #ordne opp på dette
            t += 1

    def create_letters(self, amt):
        for i in range(amt):
            self.letters.append(tk.Frame(self.root,borderwidth=2,relief="flat",bg="green",width=30,height=30))
        t = 0
        for i in self.letters:
            i.place(x=25+((self.width-25)/self.length)*t,y=80) #ordne dette
            self.actual_letters.append(tk.Label(i,text="0").place(x=7,y=2))
            t += 1
    
    def drag(self, event):
        x, y = event.x, event.y
        #print(x, y)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = App()

    app.run()