from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.title("Simple Calculator")

#iconssss
root.iconbitmap('C://recents')

my_img1 =  ImageTk.PhotoImage(Image.open("images/1.jpeg"))
my_img2=  ImageTk.PhotoImage(Image.open("images/2.jpeg"))
my_img3 =  ImageTk.PhotoImage(Image.open("images/3.jpeg"))
my_img4 =  ImageTk.PhotoImage(Image.open("images/4.jpeg"))

image_list = [my_img1, my_img2 ,my_img3, my_img4]

my_label = Label(root, image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def foward(image_number):
    global my_label
    global button_foward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number+1])

    button_foward= Button(root,text=">>", command=lambda: foward(image_number+1))
    button_back = Button(root,text="<<", command=lambda: back(image_number-1))
    
    if image_number==4:
        button_foward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_foward.grid(row=1,column=1)
    return

def back(image_number):
    global my_label
    global button_foward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number+1])

    button_foward= Button(root,text=">>", command=lambda: foward(image_number+1))
    button_back = Button(root,text="<<", command=lambda: back(image_number-1))
    return

button_back = Button(root,text="<<",  command=back)
button_foward = Button(root,text=">>", command=lambda: foward(2))
button_quit = Button(root,text="Exit Program", command=root.quit)

button_back.grid(row=1,column=0)
button_foward.grid(row=1,column=1)
button_quit.grid(row=1,column=2)

root.mainloop()