from tkinter import *
from Database import Database
from tkinter import messagebox
db = Database("store.db")


def populate_list():
    parts_list.delete(0, END)
    for rows in db.fetch():
        parts_list.insert(END, rows)


def add_item():
    if part_text.get()=="" or customer_text.get() == ""or type_text.get() == "" or price_text.get()=="":
        messagebox.showerror("Error", "Please insert info")
        return
    db.insert(part_text.get(), customer_text.get(),type_text.get(), price_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (part_text.get(), customer_text.get(),
              type_text.get(), price_text.get()))
    clear()
    populate_list()


def select_item(event):
    global remove
    index = parts_list.curselection()[0]
    remove = parts_list.get(index)
    part_entry.delete(0, END)
    part_entry.insert(END, remove[1])
    customer_entry.delete(0, END)
    customer_entry.insert(END, remove[2])
    type_entry.delete(0, END)
    type_entry.insert(END, remove[3])
    price_entry.delete(0, END)
    price_entry.insert(END, remove[4])



def remove_item():
    db.remove(remove[0])
    clear()
    populate_list()


def update_item():
    db.update(remove[0], part_text.get(), customer_text.get(),
              type_text.get(), price_text.get())
    populate_list()


def clear():
    part_entry.delete(0, END)
    customer_entry.delete(0, END)
    type_entry.delete(0, END)
    price_entry.delete(0, END)


window = Tk()
window.geometry("700x400")
window.title("PCPARTPICKER")

part_text = StringVar()
part_label = Label(window, text="Part Name", font=("Arial", 14), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(window, textvariable=part_text)
part_entry.grid(row=0, column=1)

customer_text = StringVar()
customer_label = Label(window, text="Customer", font=("Arial", 14))
customer_label.grid(row=0, column=2, sticky=W)
customer_entry = Entry(window, textvariable=customer_text)
customer_entry.grid(row=0, column=3)

type_text = StringVar()
type_label = Label(window, text="Part type", font=("Arial", 14))
type_label.grid(row=1, column=0, sticky=W)
type_entry = Entry(window, textvariable=type_text)
type_entry.grid(row=1, column=1)

price_text = StringVar()
price_label = Label(window, text="Price", font=("Arial", 14))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(window, textvariable=price_text)
price_entry.grid(row=1, column=3)
parts_list = Listbox(window, height=12, width=70)
parts_list.grid(row=3, column=1, columnspan=3, rowspan=6, pady=20, padx=20)

scroll_bar = Scrollbar(window)
scroll_bar.grid(row=4, column=4)

button_add = Button(window,text="Add part", width=12, command=add_item)
button_add.grid(row=2, column=0, pady=12)

button_update = Button(window, text="Update part", width=12, command=update_item)
button_update.grid(row=2, column=1)

button_remove = Button(window, text="Remove part", width=12, command=remove_item)
button_remove.grid(row=2, column=2)

button_clear = Button(window, text="Clear", width=12, command=clear)
button_clear.grid(row=2, column=3)

parts_list.configure(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=parts_list.yview)


parts_list.bind("<<ListboxSelect>>", select_item)

populate_list()
window.mainloop()
