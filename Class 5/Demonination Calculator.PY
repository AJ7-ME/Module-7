# libaries
from tkinter import *
from tkinter import messagebox
#from PIL import Image, ImageTk
#import os

#setting up window
root = Tk()
root.title("Demonination Calculator")
root.configure(bg='lightblue')
root.geometry("650x400")

# adding img & labels
#current_dir = os.path.dirname(__file__)
#image_path = os.path.join(current_dir, ' app_img.jpg')
#upload = Image.open(image_path)

##Resize the Image using Resize()
#upload = upload.resize((300, 300))
#image = ImageTk.PhotoImage(upload)

#label = Label(root, image=image, bg = 'lightblue')
#label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey there! Welcome to the Demonination Calculator. This calculator will help you with notes & Coins.",
    bg='lightblue',
)
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function 2 display a msgbox & continue the program
def msg():
    Msgbox = messagebox.showinfo(
        "Alert", "Do you wanna calculate the total?"
    )
    if Msgbox == 'ok':
        topwin()

# Adding a button to call the function
button1 = Button(root, text="Lets Get started!" ,command=msg,bg='brown', fg='white')
button1.place(x=260, y=360)

# Function to create a new window
def topwin():
    top = Toplevel()
    top.title("Demonination Calculator")
    top.geometry("650x450")
    top.configure(bg='light grey')

    label = Label(top, text="Enter the number of notes you have for each denomination:", bg='light grey')
    entry = Entry(top)
    lbl = Label(
        top,
        text="Here are some demoninations!",
        bg='light grey',
    )
    l1 = Label(top, text="100", bg='light grey')
    l2 = Label(top, text="50", bg='light grey')
    l3 = Label(top, text="20", bg='light grey')
    l4 = Label(top, text="10", bg='light grey')
    l5 = Label(top, text="5", bg='light grey')
    l6 = Label(top, text="2", bg='light grey')
    l7 = Label(top, text="1", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)
    t7 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note100 = amount // 100
            amount %= 100
            note50 = amount // 50
            amount %= 50
            note20 = amount // 20
            amount %= 20
            note10 = amount // 10
            amount %= 10
            note5 = amount // 5
            amount %= 5
            note2 = amount // 2
            amount %= 2
            note1 = amount // 1
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)
            t5.delete(0, END)
            t6.delete(0, END)
            t7.delete(0, END)
            t1.insert(0, str(note100))
            t2.insert(0, str(note50))
            t3.insert(0, str(note20))
            t4.insert(0, str(note10))
            t5.insert(0, str(note5))
            t6.insert(0, str(note2))
            t7.insert(0, str(note1))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
    btn = Button(top, text="Calculate", command=calculator, bg='brown', fg='white')

    label.place(x=20, y=20)
    entry.place(x=20, y=50)
    lbl.place(x=20, y=80)
    l1.place(x=20, y=110)
    t1.place(x=80, y=110)
    l2.place(x=20, y=140)
    t2.place(x=80, y=140)
    l3.place(x=20, y=170)
    t3.place(x=80, y=170)
    l4.place(x=20, y=200)
    t4.place(x=80, y=200)
    l5.place(x=20, y=230)
    t5.place(x=80, y=230)
    l6.place(x=20, y=260)
    t6.place(x=80, y=260)
    l7.place(x=20, y=290)
    t7.place(x=80, y=290)
    btn.place(x=20, y=320)
    top.mainloop()
root.mainloop()