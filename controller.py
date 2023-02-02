import model
import view
from tkinter import *
from tkinter import ttk

elements = {}

def add_number():
    view.add_number()

def add_to_list(contact):
    elements['Все контакты'].insert(END, contact)
    send_list()

def delete_from_list():
    elements['Все контакты'].delete(elements['Все контакты'].curselection()[0])
    send_list()
    
def send_list():
    contact_list = elements['Все контакты'].get(0, END)
    model.write_contacts(contact_list)

def get_elements():
    return elements



def start():
    root = Tk()
    form = ttk.Frame(root,padding=30)
    form.grid()
    
    Label(form, text='Телефонный справочник').grid(row=0, column=0)

    Label(form, text='Введите имя ').grid(row=1, column=0)
    name_entry= Entry(form)
    name_entry.grid(row=1, column=1)
    elements['Имя'] = name_entry

    Label(form, text='Введите фамилию ').grid(row=2, column=0)
    surname_entry= Entry(form)
    surname_entry.grid(row=2, column=1)
    elements['Фамилия'] = surname_entry

    Label(form, text='Введите номер телефона ').grid(row=3, column=0)
    number_entry= Entry(form)
    number_entry.grid(row=3, column=1)
    elements['Номер телефона'] = number_entry

    add_number_button = Button(form, text='Добавить контакт', command = add_number).grid(row=4, column=1)
    delete_number_button = Button(form, text='Удалить контакт', command=delete_from_list).grid(row=5, column=1)

    all_contacts = Listbox(form)
    all_contacts.grid(row=5, column=0)
    elements['Все контакты'] = all_contacts
    model.read_contacts()
    
    root.mainloop()