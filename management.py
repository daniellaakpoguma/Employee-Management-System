from tkinter import filedialog

def uploadPhoto():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=(("Image files", "*.jpg; *.jpeg; *.png"), ("All files", "*.*")))
    return file_path


