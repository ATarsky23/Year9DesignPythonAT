import tkinter as tk



from tkinter import *

canvas_width = 600
canvas_height = 600

master = Tk()

w = Canvas(master, width = canvas_width, height = canvas_height)

w.pack()

oval = w.create_oval(75,75,500,500)
minline = w.create_line(150,150,300,300)





root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )








bgcol = "#021844"
fgcol = "#FFFFFF"
root = tk.Tk()
root.configure(bg = bgcol)

#Construct
titleLabel = tk.Label(root, text = "Auto Information Filler")
#Configure

#Place
titleLabel.grid(row = 0, column = 0, columnspan = 2)
titleLabel.config(bg = bgcol, fg = fgcol, font=("Courier", 24))

entryLabel = tk.Label(root, text = "Enter your name: ")
entryLabel.grid(row = 1, column = 0)

entryName = tk.Entry(root)
entryName.grid(row = 1, column = 1)





root.mainloop()

