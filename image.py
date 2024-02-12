from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.title("Simple Calculator")

#iconssss
root.iconbitmap('C://recents')

my_img =  ImageTk.PhotoImage(Image.open("jollof-rice.jpg"))
label = Label(root, image=my_img)
label.pack()


button_quit = Button(root,text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()