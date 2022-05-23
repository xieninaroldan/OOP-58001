from tkinter import *

window = Tk()
window.title("Finding Smallest Number")
window.geometry("550x350+20+100")

def FindTheSmallestNumber():
    L = []
    L.append(eval(Number1.get()))
    L.append(eval(Number2.get()))
    L.append(eval(Number3.get()))
    LeastNumber.set(min(L))

#labels

label1 = Label(window, text = "Find the least number among three numbers",justify='center')
label1.grid(row=0, column=1,pady=5)

label2 = Label(window,text = "Enter the first number:")
label2.grid(row=1, column = 0,sticky=W,pady=5, padx=5)

label3 = Label(window,text = "Enter the second number:")
label3.grid(row=2, column=0, pady=5, padx=5)

label4 = Label(window,text="Enter the third number:")
label4.grid(row=3,column =0, sticky=W, pady=5, padx=5)

label5 = Label(window,text="The smallest number:")
label5.grid(row=5,column=0,sticky=W, pady=5, padx=5)

#entry

Number1 = StringVar()
entry1 = Entry(window,bd=3,textvariable=Number1)
entry1.grid(row=1, column = 1, pady=5, padx=5)

Number2 = StringVar()
entry2 = Entry(window,bd=3,textvariable=Number2)
entry2.grid(row=2,column=1, pady=5, padx=5)

Number3 = StringVar()
entry3 = Entry(window,bd=3,textvariable=Number3)
entry3.grid(row=3, column=1, pady=5, padx=5)

LeastNumber = StringVar()
entry4 = Entry(window,bd=3,state="readonly",textvariable=LeastNumber)
entry4.grid(row=5,column=1, pady=5, padx=5)

#button

button1 = Button(window,text = "The smallest number among the three is:",command = FindTheSmallestNumber)
button1.grid(row=4, column = 1, pady=5, padx=5)

mainloop()