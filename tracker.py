from tkinter import * 

root = Tk()

def myClick():
    myLabel = Label(root, text="Look, i cliked the button!")
    myLabel.pack()

myButton = Button(root, text="Click Me", command=myClick, bg="blue")
myButton.pack()
myButton.grid()

root.mainloop()
