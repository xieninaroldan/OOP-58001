from tkinter import *
from tkinter import ttk
window = Tk()
window.geometry("500x250+10+20")
window.title("Midterm in OOP")

label = Label(window, text = "Enter your fullname:", fg = "red")
label.place(x=60, y=70)

txtfld = Entry(window, bd = 5)
txtfld.place(x=265, y=65)

button = Button(window, text = "Click to display your Fullname", fg = "red")
button.place(x=60, y=145)

txtfld = Entry(window, bd = 5)
txtfld.place(x=265, y=150)

window.mainloop()
