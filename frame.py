from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Frame")

frame = LabelFrame(root, text="THIS IS MY FRAME", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="True Button")
b.pack()

root.mainloop()
