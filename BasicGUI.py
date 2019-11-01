import tkinter as tk 


def onclick():
	print("Luca is good at 2k")

print("Start Program")
root = tk.Tk() #builds your main window

#Widget/Element is an element in a GUI
#Button, Textbox, Input box, Slider, Drop down, Image
#Step 1: Costruct the widget.
btn1 = tk.Button(root, width = 100, height = 3)
#Step 2: Configure the button
btn1.config(text="I am a button")
#Step 3: Place the widget-pack(), grid()
btn1.pack()

btn2 = tk.Button(root, width = 75, height = 2, command = onclick)
#Step 2: Configure the button
btn2.config(text="click me")
#Step 3: Place the widget-pack(), grid()
btn2.pack() 

self.button = Button(self,text="Click Me",command=self.color_change,bg="blue")
self.button.grid(row = 2, column = 2, sticky = W)


output = tk.Text(root, width = 100, height = 20)
output.config()
output.pack();

root.mainloop()

print("END PROGRAM")