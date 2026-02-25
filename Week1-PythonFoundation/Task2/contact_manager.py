FILE_NAME = "contacts.txt"


def add_contact(name, phone):
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone}\n")


def view_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contacts found.")


add_contact("Ali", "03001234567")
view_contacts()
