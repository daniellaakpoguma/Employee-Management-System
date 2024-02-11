from tkinter import * 

root = Tk()

e = Entry(root, bg = "blue", width=50)
e.pack()
e.insert(0,"Enter Your Name:")

def myClick():
    hello = "Hello" + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Click Me", command=myClick, bg="blue")
myButton.pack()

root.mainloop()
