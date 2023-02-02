import view

def write_contacts(contact_list):
    data = open('Phonebook.txt', mode = 'w' ,encoding='utf-8')
    for contact in contact_list:
        data.writelines(contact + '\n')
    data.close()


def read_contacts():
    data = open('Phonebook.txt', mode = 'r' ,encoding='utf-8')
    contact_list= data.readlines()
    view.print_contact_list(contact_list)
    data.close()
