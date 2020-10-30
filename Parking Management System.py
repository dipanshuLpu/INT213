from tkinter import *
from tkinter import messagebox
import time
import sys
from db import Database

db = Database('store.db')


def populate_list():
    pms_list.delete(0, END)
    for row in db.fetch():
        pms_list.insert(END, row)


def add_item():
    if part_text.get() == '' or customer_text.get() == '' or vnumber_text.get() == '' or time_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(part_text.get(), customer_text.get(),
              vnumber_text.get(), time_text.get())
    pms_list.delete(0, END)
    pms_list.insert(END, (part_text.get(), customer_text.get(),
                            vnumber_text.get(), time_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = pms_list.curselection()[0]
        selected_item = pms_list.get(index)

        part_entry.delete(0, END)
        part_entry.insert(END, selected_item[1])
        customer_entry.delete(0, END)
        customer_entry.insert(END, selected_item[2])
        vnumber_entry.delete(0, END)
        vnumber_entry.insert(END, selected_item[3])
        time_entry.delete(0, END)
        time_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], part_text.get(), customer_text.get(),
              vnumber_text.get(), time_text.get())
    populate_list()


def clear_text():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    vnumber_entry.delete(0, END)
    time_entry.delete(0, END)


# Create window object
app = Tk()

# Part
part_text = StringVar()
part_label = Label(app,bg="steel blue",fg="white", text='   Wheeler →', font=('arial',15), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)
# Customer
customer_text = StringVar()
customer_label = Label(app,bg="steel blue",fg="white", text='      Owner Name →', font=('arial', 15))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)
# vnumber
vnumber_text = StringVar()
vnumber_label = Label(app,bg="steel blue",fg="white", text=' Vehicle No →', font=('arial', 15))
vnumber_label.grid(row=1, column=0, sticky=W)
vnumber_entry = Entry(app, textvariable=vnumber_text)
vnumber_entry.grid(row=1, column=1)
# time
time_text = StringVar()
time_label = Label(app,bg="steel blue",fg="white", text='  Vehicle Entry Time →', font=('arial', 15))
time_label.grid(row=1, column=2, sticky=W)
time_entry = Entry(app, textvariable=time_text)
time_entry.grid(row=1, column=3)
# pms List (Listbox)
pms_list = Listbox(app, height=8, width=50, border=0)
pms_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
pms_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=pms_list.yview)
# Bind select
pms_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Register vehicle',bg="green",fg="white",font=('arial',10), width=13, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Check out Vehicle',bg="Red",fg="white",font=('arial',10), width=15, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update Information',bg="Blue",fg="white",font=('arial',11), width=17, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Information',bg="yellow",fg="black",font=('arial',11), width=15, command=clear_text)
clear_btn.grid(row=2, column=3)

Dev_label = Label(app,bg="steel blue",fg="white", text='               Parking History', font=('arial',11)).place(x=120,y=157)

Dev_label = Label(app,bg="steel blue",fg="white", text='PARKING MANAGEMENT SYSTEM', font=('arial',14)).place(x=75,y=322)

Dev_label = Label(app,bg="steel blue",fg="white", text='How To Use :', font=('arial',14)).place(x=670,y=19)

app.title('Parking Management System')
app.geometry('1010x470')
app.configure(bg='steel blue')
Dev_label = Label(app,bg="steel blue",fg="white", text='Dipanshu,Priya,Kartik', font=('arial',12)).place(x=9,y=440)
canvas = Canvas(app, width=200, height=200, bg="white")


Dev_label = Label(app,bg="steel blue",fg="white", text='Enter all information and register.', font=('arial',12)).place(x=670,y=70)
Dev_label = Label(app,bg="steel blue",fg="white", text='Click check out when checking out vehicle.', font=('arial',12)).place(x=670,y=94)
Dev_label = Label(app,bg="steel blue",fg="white", text='All Registered vehicled will be shown in History.', font=('arial',12)).place(x=670,y=94)

canvas = Canvas(app, width=200, height=200, bg="white")

   
button_quit = Button(app, text="          Exit         ",bg="Black",fg="white",font=('arial',12), command = app.destroy).place(x=860, y=415)

           


# Populate data
populate_list()

# Start program
app.mainloop()



