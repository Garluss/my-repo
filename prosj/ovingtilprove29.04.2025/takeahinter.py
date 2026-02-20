import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

img = Image.open("Tkinter/funny.jpg")
img = img.resize((100,100))
img = ImageTk.PhotoImage(img)

tk.Label(root,text="Trykk på kun én!",borderwidth=20,width=20).grid(row=0,column=0,columnspan=3)
tk.Button(root,text="Hei",command=lambda: print("Hei")).grid(row=1,column=0,pady=2)
tk.Button(root,text="Hade",command=lambda: print("Hade")).grid(row=1,column=1,pady=2)
tk.Button(root,text="...",command=lambda: print("...")).grid(row=1,column=2,pady=2)
tk.Label(root,image=img).grid(row=2,column=1)

root.mainloop()