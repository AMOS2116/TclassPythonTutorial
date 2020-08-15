# Tkinter is a graphical User Interfase module for python. it is a standard pyhton interface

# How to create an application using tkinter
'''
Import the module-tkinter
Create the main window(container)
Add any number of widgets to the main window
Apply the event Trigger on the widgets
'''

from tkinter import *

window = Tk()

# add widgets here

# Button widget
btn = Button(window, text = 'This is a button widget', fg = 'green')
btn.place(x = 80, y = 100)

# Label widget
lbl = Label(window, text = 'This is a label widget', fg = 'red', font = ('Helvetica', 16))
lbl.place(x = 60, y = 50)

# Entry widget
txtfld = Entry(window, text = 'This is an entry widget', bd = 5)
txtfld.place(x = 80, y = 150)

window.title('Welcome to Tclassified.com ICT Center')
window.geometry('400x300+10+20')
window.mainloop()