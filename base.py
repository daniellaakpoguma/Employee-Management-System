from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Base")
root.geometry("400x400")

def show():
    myLabel = myLabel = Label(root, text=clicked.get()).pack()

#checboxes
var = StringVar()
c = Checkbutton(root, text="Check this box", variable=var, onvalue="on", offvalue="off")
c.deselect()
c.pack()
myLabel = Label(root, text=var.get()).pack()
myButton = Button(root, text="Show Selection", command=show).pack()

options = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Fridat", "Saturday"
]
#drop down boxes
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

root.mainloop()