from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

root = Tk()
root.title("Radio Buttons")

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World")
    Label(root, text=response).pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()