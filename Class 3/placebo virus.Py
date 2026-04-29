from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("400x200")
def a():
    messagebox.showwarning("ALERT VIRUS DETECTED SEND ME $20 TO MAKE IT DISAPPEAR")
button = Button(root, text="Scan for a Virus send 15 dollars and none will be found :)", command=a)
button.place(x = 40, y = 80)
root.mainloop()