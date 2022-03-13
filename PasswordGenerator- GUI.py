import tkinter as tk
import tkinter.messagebox
from tkinter import *
import random
import string
import sys


def guiwindow():
    window = tk.Tk()
    window.title("Password Generator v1.0")
    window.geometry("400x300")
    window.resizable(False, False)

    Label(window, text="Password Generator v1.0").place(
        relx=0.5, rely=0.1, anchor=CENTER)

    var1 = IntVar()
    Checkbutton(window, text="number", variable=var1, onvalue=1,
                offvalue=0).place(relx=0.5, rely=0.2, anchor=CENTER)

    var2 = IntVar()
    Checkbutton(window, text="letter", variable=var2, onvalue=1,
                offvalue=0).place(relx=0.5, rely=0.3, anchor=CENTER)

    var3 = IntVar()
    Checkbutton(window, text="special characters", variable=var3,
                onvalue=1, offvalue=0).place(relx=0.5, rely=0.4, anchor=CENTER)

    def callback(input):
        if input.isdigit() or input == "":
            return True
        else:
            return False

    tk.Label(window, text="Number of characters").place(
        relx=0.5, rely=0.5, anchor=E)
    ent1 = tk.Entry(window)
    ent1.place(relx=0.5, rely=0.5, anchor=W)

    reg = window.register(callback)
    ent1.config(validate="key", validatecommand=(reg, '%P'))

    tk.Label(window, text="Password").place(
        relx=0.5, rely=0.6, anchor=E)
    ent2 = tk.Entry(window)
    ent2.place(relx=0.5, rely=0.6, anchor=W)

    def randomlists():
        special_char = '@_!#$%^&*()<>?/\|}{~:;[]'
        characterslist = list(special_char)
        letterlist = list(string.ascii_letters + string.ascii_letters)
        numlist = list(string.digits + string.digits)
        total_length = int(ent1.get())
        if var1.get() == 0:
            numlist = list()
        if var2.get() == 0:
            letterlist = list()
        if var3.get() == 0:
            characterslist = list()
        multilist = list(characterslist+letterlist+numlist)
        random.shuffle(multilist)
        password = []
        for i in range(total_length):
            password.append(random.choice(multilist))
        final = "".join(password)
        ent2.insert(0, final)

    def generation():
        if var1.get() == 0 & var2.get() == 0 & var3.get() == 0:
            tkinter.messagebox.showinfo("Error", "Select the Options")
        elif len(ent1.get()) == 0:
            tkinter.messagebox.showinfo(
                "Error", "Choose a number of characters")
        elif len(ent2.get()) > 0:
            ent2.delete(0, 'end')
            randomlists()
        else:
            randomlists()

    tk.Button(window, text='Generate', command=generation).place(
        relx=0.5, rely=0.7, anchor=CENTER)

    def exitbutton():
        sys.exit()

    Button(window, text='Quit', command=exitbutton).place(
        relx=0.5, rely=0.8, anchor=CENTER)

    mainloop()


guiwindow()
