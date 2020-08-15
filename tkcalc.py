from tkinter import *

class SimpleAddCal:
    def __init__(self, win):
        # Labels
        self.lbl1 = Label(win, text = "First Number")
        self.lbl1.place(x = 100, y = 50)
        self.lbl2 = Label(win, text = "Second Number")
        self.lbl2.place(x = 100, y = 100)
        self.lbl3 = Label(win, text = "Result")
        self.lbl3.place(x = 100, y = 200)
        # Entries
        self.t1 = Entry(bd = 3)
        self.t2 = Entry()
        self.t3 = Entry()

        self.t1.place(x = 200, y = 50)
        self.t2.place(x = 200, y = 100)
        self.t3.place(x = 200, y = 200)

         # Butoons
        self.btn1 = Button(win, text = 'Add', command = self.add)
        self.btn2 = Button(win, text = 'Subtract', command = self.sub)
       

        self.btn1.place(x = 100, y = 150)
        self.btn2.place(x = 200, y = 150)

        # Trigger
          # Addition Trigger

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

          # Subtract Trigger

    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))
       



window = Tk()
mywin = SimpleAddCal(window)
window.title('Tclassified.com Calculator')
window.geometry('500x400+10+10')
window.mainloop()