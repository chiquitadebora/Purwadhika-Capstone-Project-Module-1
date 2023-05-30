from datetime import datetime

# last_id = 0
all_contacts = [
    {
        "id": 1,
        "name": "Billy",
        "phone": "089765435567",
        "email": "billy@gmail.com",
        "created_at": "34567"
    },
    {
        "id": 2,
        "name": "Bella",
        "phone": "+6281914562746",
        "email": "bella@gmail.com",
        "created_at": "56789"
    },
    {
        "id": 3,
        "name": "Jessica",
        "phone": "089723458876",
        "email": "jessica@gmail.com",
        "created_at": "78906"
    }
]


def print_main_menu():
    print('==========================================')
    print('Yellow Pages Menu')
    print('==========================================')
    print('1. Read Contact')
    print('2. Create Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Exit')
    print('==========================================')


# read input from user and then return the value
def read_user_input():
    str_option = input(" -> ")
    option = int(str_option)
    return option


# print contact <id>. <name> - <phone>
def print_contact(contact):
    id = contact["id"]
    name = contact["name"]
    phone = contact["phone"]
    print("\t{}. {} - {}".format(id, name, phone))

# show contact if user input 1,1


def show_contacts():
    print("\tAll Contacts:")
    for contact in all_contacts:
        print_contact(contact)


def filter_contacts(criteria):
    result = []
    for contact in all_contacts:
        if criteria.lower() in contact["name"].lower():
            result.append(contact)
    return result


def print_read_menu():
    print("1. Show All Contact")
    print("2. Search Contact")
    print("3. Exit")


def execute_read_menu():
    option = read_user_input()
    if option == 1:
        show_contacts()
    elif option == 2:
        search = input("Search: ")
        search_result = filter_contacts(search)
        if len(search_result) > 0:
            for contact in search_result:
                print_contact(contact)
        else:
            print("Data not found.")


def print_create_menu():
    print("1. Add Data")


def input_id():
    return input("Insert id for the contact : ")


def input_name():
    return input("Insert contact name : ")


def input_phone():
    return input("Insert phone number : ")


def input_email():
    return input("Insert email : ")


def execute_create_menu():
    option = read_user_input()
    if option == 1:
        id = int(input_id())
        for contact in all_contacts:
            if id == contact["id"]:
                print("Data already exist")
                return

        name = input_name()
        phone = input_phone()
        email = input_email()
        created_at = str(datetime.now())

        new_contact = {
            "id": id,
            "name": name,
            "phone": phone,
            "email": email,
            "created_at": created_at
        }

        all_contacts.append(new_contact)
        print("Contact", name, "Added")


def print_update_menu():
    print("1. Update Data")
    print("2. Back to Main Menu")


def print_delete_menu():
    print("1. Delete Data")
    print("2. Back to Main Menu")


def execute_delete_menu():
    option = read_user_input()
    if option == 1:
        id = int(input("Input ID you want to delete : "))
        for index in range(len(all_contacts)):
            contact = all_contacts[index]
            contact_id = contact["id"]
            if id == contact_id:
                deleted_contact = all_contacts.pop(index)
                print("Contact", deleted_contact["name"], "deleted.")
                return
        print("Data not found")


def execute_update_menu():
    option = read_user_input()
    if option == 1:
        id = int(input("Input ID you want to update : "))
        for index in range(len(all_contacts)):
            contact = all_contacts[index]
            contact_id = contact["id"]
            if id == contact_id:
                updated_name = input_name()
                updated_phone = input_phone()
                updated_email = input_email()

                all_contacts[index]["name"] = updated_name
                all_contacts[index]["phone"] = updated_phone
                all_contacts[index]["email"] = updated_email
                return
        print("Data not found")

# execute given option, then return a boolean that indicates wether the program should stop or continue


def execute_option(option: int):
    program_should_stop = False

    if option == 1:
        print_read_menu()
        execute_read_menu()
    elif option == 2:
        print_create_menu()
        execute_create_menu()
    elif option == 3:
        print_update_menu()
        execute_update_menu()
    elif option == 4:
        print_delete_menu()
        execute_delete_menu()
    elif option == 5:
        print("Exited")
        program_should_stop = True
    else:
        print("wrong option")

    return program_should_stop


def main_loop():
    while True:
        print_main_menu()
        choosen_option = read_user_input()
        program_should_stop = execute_option(choosen_option)
        if program_should_stop:
            break


main_loop()
