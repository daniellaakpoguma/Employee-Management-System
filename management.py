from tkinter import filedialog
import re

def validatePhoneNumber(phoneNumber_entry):
    phoneNumber = phoneNumber_entry.get()
    pattern = r'^\d{3}-?\d{3}-?\d{4}$'  # Regular expression pattern for a typical North American phone number
    if re.match(pattern, phoneNumber):
        phoneNumber_entry.config(bg="gray")  # Set background color to white for valid phone number
        return True
    else:
        phoneNumber_entry.config(bg="red")  # Set background color to red for invalid phone number
        return False


def uploadPhoto():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=(("Image files", "*.jpg; *.jpeg; *.png"), ("All files", "*.*")))
    return file_path


