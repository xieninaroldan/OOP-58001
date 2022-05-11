from tkinter import *

def Calc(source, side):
    storeObj = Frame(source, borderwidth = 4, bd = 4, bg= "powder blue")
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj

def button(source, side, text, command = None):
    storeObj = Button(source, text = text, command = command)
    storeObj.pack(side = side, expand = YES, fill = BOTH)
    return storeObj

class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'arial 20 bold')
        self.pack(expand = YES, fill = BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self, relief = RIDGE, textvariable = display,justify = 'right', bd = 30, bg = "powder blue").pack(side = TOP, expand = YES, fill = BOTH)

        for clearButton in (["C"]):
            erase = Calc(self, TOP)
            for char in clearButton:
                button(erase, LEFT, char, lambda storeObj = display, q = char: storeObj.set(''))

        for numButton in ("789/", "456*", "123-", "0.+"):
            FunctionNum = Calc(self, TOP)
            for Equals in numButton:
                button(FunctionNum, LEFT, Equals, lambda storeObj = display, q = Equals: storeObj.set(storeObj.get() + q))

        EqualButton = Calc(self, TOP)
        for Equals in "=":
            if Equals == '=':
                ButtonEquals = button(EqualButton, LEFT, Equals)
                ButtonEquals.bind('<ButtonRelease-1>', lambda e, s = self, storeObj = display: s.calc(storeObj), '+')

            else:
                ButtonEquals = button(EqualButton, LEFT, Equals, lambda storeObj = display, s=' %s ' % Equals: storeObj.set(storeObj.get() + s))

    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")


if __name__ == '__main__':
    Calculator().mainloop()