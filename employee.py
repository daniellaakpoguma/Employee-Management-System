from tkinter import * 
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from management import uploadPhoto

root = Tk()
root.title("Employee Management System")
root.geometry("800x1000") # Size of window

#Title Bar
custom_color_red = "#BD1D1D"
# Create the title frame with a red background
titleFrame = Frame(root, bg=custom_color_red)
# Create the title label and place it in the title frame
titleLabel = Label(titleFrame, text="COREF Management System", bg=custom_color_red, fg="white",  font=("TkDefaultFont", 25)) 
titleLabel.pack(side="left", padx=10)
# Create the logout button and place it in the title frame
logoutButton = Button(titleFrame, text="Logout")
logoutButton.pack(side="right", padx=10)
titleFrame.pack(fill="x") 

#Menu Bar
menuFrame = Frame(root, bg="#F8C321", width=200)

# Profile picture 
image = Image.open("images/defaultPic.jpeg")
photo = ImageTk.PhotoImage(image)
defaultPhoto = Label(menuFrame, image=photo)
defaultPhoto.place(x=20, y=20)
#profile picture end

profileText = Label(menuFrame, text = "Your Profile", fg = "black",bg="#F8C321", font=("TkDefaultFont", 20))
profileText.place(x=40, y=180)
menuFrame.pack(side="left", fill="y", expand=False)
menuFrame.pack_propagate(False)

#Employee Information Bar

# Personal Title
personalTitle = Label(root, text="Personal Details", font=("TkDefaultFont", 20))
personalTitle.pack()

# row 1
firstNameLabel = Label(root, text= "First Name:").place(x=210, y=70)
middleNameLabel = Label(root, text= "Middle Name:").place(x=400, y=70)
lastNameLabel = Label(root, text= "Last Name:").place(x=600, y=70)
firstNameEntry = Entry(root).place(x=285, y= 67, width= 100)
middleNameEntry = Entry(root).place(x=490, y= 67, width= 100)
lastNameLabel = Entry(root).place(x=680, y= 67, width= 110)

#row 2
genderLabel = Label(root, text="Gender:").place(x=210, y=100)
genderVar = IntVar()
genderVar.set("Not disclosed") 
genderOptions = ["Male", "Female", "Non-Binary"]
genderCheckbox = gender_menu = OptionMenu(root, genderVar, *genderOptions).place(x=265, y=100,width= 130)
phoneOneLabel  = Label(root, text= "Phone 1:").place(x=400, y=100)
phoneOneEntry = Entry(root).place(x=460, y= 100, width= 130)
phoneTwoLabel  = Label(root, text= "Phone 2:").place(x=600, y=100)
phoneTwoEntry = Entry(root).place(x=660, y= 100, width= 130)

#row 3
emailLabel = Label(root, text="Email:").place(x=210, y=130)
emailEntry = Entry(root).place(x=255, y= 130, width= 250)
photoLabel = Label(root, text="Photo:").place(x=510, y=130)
uploadButton = Button(root, text="Upload Photo", command=uploadPhoto)
uploadButton.place(x=560, y=130)

# row 4
street1Label = Label(root, text="Street 1:").place(x=210, y=160)
street1Entry = Entry(root).place(x=270, y= 160, width= 520)
street2Label = Label(root, text="Street 2:").place(x=210, y=190)
street2Entry = Entry(root).place(x=270, y= 190, width=520)
cityLabel = Label(root, text="City:").place(x=210, y=220)
cityEntry = Entry(root).place(x=245, y= 220, width=120)
provinces = [
    "Alberta", "British Columbia", "Manitoba", "New Brunswick", 
    "Newfoundland and Labrador", "Nova Scotia", "Ontario", 
    "Prince Edward Island", "Quebec", "Saskatchewan", "Northwest Territories", 
    "Nunavut", "Yukon"
]
# Create a variable to store the selected province
province_var = StringVar()
provinceLabel = Label(root, text="Province:").place(x=365, y=220)
provinceDropdown = OptionMenu(root, province_var, *provinces)
province_var.set("Alberta")
provinceDropdown.place(x=430, y= 220, width= 180)
postalCodeLabel = Label(root, text="Postal Code:").place(x=610, y=220)
postalCodeEntry = Entry(root).place(x=695, y= 220, width= 95)

# Work Details
workTitle = Label(root, text="Work Details", font=("TkDefaultFont", 20))
workTitle.place(x=440, y= 250)

#row 1
employeeIDLabel = Label(root, text="Employee ID:").place(x=210, y= 280)
employeeIDEntry = Entry(root).place(x=297, y= 280, width= 95)
titleLabel = Label(root, text="Title:").place(x=392, y= 280)
titleEntry = Entry(root).place(x=430, y= 280, width= 150)
departmentLabel = Label(root, text="Department:").place(x=580, y= 280)
departmentEntry = Entry(root).place(x=660, y= 280, width= 130)

# row 2
startDateLabel = Label(root, text="Start Date:").place(x=210, y= 310)
startDateEntry = DateEntry(root).place(x=280, y= 310, width=100)
endDateLabel = Label(root, text="End Date:").place(x=385, y= 310)
endDateEntry = DateEntry(root).place(x=450, y= 310, width=100)
salaryLabel  = Label(root, text="Salary:").place(x=550, y= 310)
salaryEntry =  Entry(root).place(x= 600, y= 310, width= 190)

# Performance and Training
perfomanceTitle = Label(root, text="Performance & Training", font=("TkDefaultFont", 20))
perfomanceTitle.place(x=400, y= 340)
perfomanceReviewsLabel = Label(root, text="Performance Reviews").place(x=210, y= 370)
performanceEntry = Entry(root).place(x=210, y= 400, width=580, height=200)

# Leave and Attendance
leaveTitle = Label(root, text="Leave & Attedance", font=("TkDefaultFont", 20))
leaveTitle.place(x=400, y= 605)
vacationDaysLabel =  Label(root, text="Vacation Days:").place(x=290, y= 635)
vacationDaysEntry =  Entry(root).place(x=390, y= 635, width=80)
sickLeaveLabel =  Label(root, text="Sick Leave:").place(x=500, y= 635)
sickLeaveEntry =  Entry(root).place(x=575, y= 635, width=80)


root.mainloop()