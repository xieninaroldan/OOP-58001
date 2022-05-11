from tkinter import *

window = Tk()

def compute():
    txtfld4.delete(0, 'end')
    prelims = int(txtfld1.get())
    midterms = int(txtfld2.get())
    finals = int(txtfld3.get())
    total = (prelims + midterms + finals) / 3
    txtfld4.insert(END, str(total))

window.title("Semestral Grade of a Student")
window.geometry("800x300")

label1 = Label(window, text="Prelims:")
label1.place(x=70, y=50)
txtfld1 = Entry(window, bd=3)
txtfld1.place(x=180, y=50)

label2 = Label(window, text="Midterms:")
label2.place(x=70, y=80)
txtfld2 = Entry(window, bd=3)
txtfld2.place(x=180, y=80)

label3 = Label(window, text="Finals:")
label3.place(x=70, y=110)
txtfld3 = Entry(window, bd=3)
txtfld3.place(x=180, y=110)

label4 = Label(window, text="Semestral Grade:")
label4.place(x=70, y=220)
txtfld4 = Entry(window, bd=3)
txtfld4.place(x=180, y=220)

button = Button(window, text="Compute the Semestral Grade", command=compute)
button.place(x=100, y=165)

label5 = Label(window, text="Grade Point and Letter Equivalent with Description:")
label5.place(x=400, y=30)

label6 = Label(window, text="97-100%        1.00        A           Excellent")
label6.place(x=430, y=60)

label7 = Label(window, text="93-96%          1.25        A-         Superior")
label7.place(x=430, y=80)

label8 = Label(window, text="89-92%          1.50        B+        Superior")
label8.place(x=430, y=100)

label9 = Label(window, text="85-88%          1.75        B           Average")
label9.place(x=430, y=120)

label10 = Label(window, text="82-84%          2.00        B-         Average")
label10.place(x=430, y=140)

label11 = Label(window, text="79-81%          2.25        C+        Average")
label11.place(x=430, y=160)

label12 = Label(window, text="76-78%          2.50        C           Passed")
label12.place(x=430, y=180)

label13 = Label(window, text="73-75%          2.75        C-         Passed")
label13.place(x=430, y=200)

label14 = Label(window, text="70-72%          3.00        D           Passed")
label14.place(x=430, y=220)

label15 = Label(window, text="70 below       5.00         F           Failed")
label15.place(x=430, y=240)


window.mainloop()