from tkinter import *
from tkinter import ttk
root = Tk()
#creates a label widget
mylabel1 = Label(root, text="Hello World!")
mylabel2 = Label(root, text="My name is jonah casey")
#shoving it onto the screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1, collumn=0)


root.mainloop()

