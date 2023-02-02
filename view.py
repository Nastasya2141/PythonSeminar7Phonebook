import controller
from tkinter import *

def add_number():
    elements = controller.get_elements()
    name = elements['Имя'].get()
    surname = elements['Фамилия'].get()
    phone_number = elements['Номер телефона'].get()

    contact = f'{name} {surname} - {phone_number}'
    controller.add_to_list(contact)


def print_contact_list(contact_list):
    for contact in contact_list:
        controller.add_to_list(contact)

