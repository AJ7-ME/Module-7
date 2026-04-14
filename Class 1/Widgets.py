from tkinter import *
from datetime import date
root = Tk()
root.title('Widgits')
root.geometry('400x300')
lbl = Label(text="Hey there!", fg="white", bg="#6BFF6B", height=1, width=300)
name_lbl = Label(text="What is your name?", bg="#B7FF00")
name_entry = Entry()
def display():
    name = name_entry.get()
    name = name[0].upper() + name[1:].lower()
    global message 
    message = "welcome to Widgits! \n Todays date is:"
    greet = "Hello "+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height=3)
btn = Button(text="Begin", command=display, height=1, bg="#73FF00", fg='white')
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()