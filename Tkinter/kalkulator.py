import tkinter as tk
from tkinter import font

eq = ""
ans = ""
def append(n):
    global eq
    eq = eq + n
    label.configure(text=eq)

def add(a,b):
    return int(a) + int(b)

def multiply(a,b):
    return int(a)*int(b)

def divide(a,b):
    return int(a)/int(b)

def calculate():
    global eq
    cmd = eq.split()
    for i in range(cmd.count("*")):
        ind = cmd.index("*")
        if "/" in cmd:
            ind2 = cmd.index("/")
            if ind2 < ind:
                continue
        new = multiply(cmd[ind-1],cmd[ind+1])
        for y in range(3):
            cmd.pop(ind-1)
        cmd.insert(0,new)
    for i in range(cmd.count("/")):
        ind = cmd.index("/")
        if "*" in cmd:
            ind2 = cmd.index("*")
            if ind2 < ind:
                continue
        new = divide(cmd[ind-1],cmd[ind+1])
        for y in range(3):
            cmd.pop(ind-1)
        cmd.insert(0,new)
    for i in range(cmd.count("+")):
        ind = cmd.index("+")
        new = add(cmd[ind-1],cmd[ind+1])
        for y in range(3):
            cmd.pop(ind-1)
        cmd.insert(0,new)


    label.configure(text=cmd)
    ans = str(cmd[0])
    eq = ""
    cmd.clear()


root = tk.Tk()

defaultfont = font.nametofont("TkDefaultFont")
defaultfont.configure(family="Comic Sans MS", size=20)

label = tk.Label(root, text="",bg="blue",width=20)
label.grid(row=0,column=1,pady=10)

tk.Button(root,text="1",width=3,command=lambda: append("1")).grid(row=1,column=0,padx=5,pady=5)
tk.Button(root,text="2",width=3,command=lambda: append("2")).grid(row=1,column=1,padx=5,pady=5)
tk.Button(root,text="3",width=3,command=lambda: append("3")).grid(row=1,column=2,padx=5,pady=5)
tk.Button(root,text="+",width=3,command=lambda: append(" + ")).grid(row=1,column=3,padx=5,pady=5)

tk.Button(root,text="4",width=3,command=lambda: append("4")).grid(row=2,column=0,padx=5,pady=5)
tk.Button(root,text="5",width=3,command=lambda: append("5")).grid(row=2,column=1,padx=5,pady=5)
tk.Button(root,text="6",width=3,command=lambda: append("6")).grid(row=2,column=2,padx=5,pady=5)
tk.Button(root,text="/",width=3,command=lambda: append(" / ")).grid(row=2,column=3,padx=5,pady=5)

tk.Button(root,text="7",width=3,command=lambda: append("7")).grid(row=3,column=0,padx=5,pady=5)
tk.Button(root,text="8",width=3,command=lambda: append("8")).grid(row=3,column=1,padx=5,pady=5)
tk.Button(root,text="9",width=3,command=lambda: append("9")).grid(row=3,column=2,padx=5,pady=5)
tk.Button(root,text="*",width=3,command=lambda: append(" * ")).grid(row=3,column=3,padx=5,pady=5)

tk.Button(root,text="0",width=3,command=lambda: append("0")).grid(row=4,column=1,padx=5,pady=5)
tk.Button(root,text="=",width=3,command=calculate).grid(row=4,column=3,padx=5,pady=5)

root.mainloop()