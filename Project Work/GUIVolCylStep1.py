import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import messagebox



#Varuibles
bgcol = "#021844"
fgcol = "#FFFFFF"





#Functions
def pushTheButton():
    messagebox.showinfo("Outcome of pushing the button", " You have pushed the button!")






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


entryemail = tk.Label(root, text = "Enter your email: ")
entryemail.grid(row = 2, column = 0)

entryName2 = tk.Entry(root)
entryName2.grid(row = 2, column = 1)

entryCard = tk.Label(root, text = "Credit card number:")
entryCard.grid(row = 3, column = 0)

entryCard = tk.Entry(root)
entryCard.grid(row = 3, column = 1)

entryAdress = tk.Label(root, text = "Enter your addresse:")
entryAdress.grid(row = 4, column = 0)

entryAdress = tk.Entry(root)
entryAdress.grid(row = 4, column = 1)

entryCVV = tk.Label(root, text = "Enter CVV:")
entryCVV.grid(row = 5, column = 0)

entryCVV = tk.Entry(root)
entryCVV.grid(row = 5, column = 1)

entryCity = tk.Label(root, text = "Enter your city:")
entryCity.grid(row = 6, column = 0)

entryCity = tk.Entry(root)
entryCity.grid(row = 6, column = 1)

entryPostal = tk.Label(root, text = "Enter postal code:")
entryPostal.grid(row = 7, column = 0)

entryPostal = tk.Entry(root)
entryPostal.grid(row = 7, column = 1)


entryExpirery = tk.Label(root, text = "Credit card expiery:")
entryExpirery.grid(row = 8, column = 0)

entryExpirery = tk.Entry(root)
entryExpirery.grid(row = 8, column = 1)



buttons = []#This creates a list 

#Constructs the buttons
for i in range(0,8,1):
	buttons.append(Button(root, text = "Save", command = pushTheButton))


#Add the buttons
for i in range(0,8,1):
	buttons[i].grid(row = 1 + i, column = 2, )

root.mainloop()