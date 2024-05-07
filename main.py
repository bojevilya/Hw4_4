def parse_input(user_input):         # Розбиває рядок вводу на команду та аргументи.
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):     # додає новий контакт
    if len(args) != 2:
        return "Invalid format. Usage: add [name] [phone number]"

    name, phone = args
    if name in contacts:
        return f"Contact '{name}' already exists. Use 'change' to update."

    contacts[name] = phone
    return f"Contact '{name}' added."

def change_contact(args, contacts):    # Змінює номер телефону для існуючого контакту
    if len(args) != 2:
        return "Invalid format. Usage: change [name] [new phone number]"

    name, new_phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."

    contacts[name] = new_phone
    return f"Contact '{name}' updated."

def show_phone(args, contacts):  # Виводить номер телефону контакта
    if len(args) != 1:
        return "Invalid format. Usage: phone [name]"

    name = args[0]
    if name not in contacts:
        return f"Contact '{name}' not found."

    return contacts[name]

def show_all(contacts): # Виводить всі збережені контакти з номерами телефонів

    if not contacts:
        print("No contacts found.")
        return

    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    contacts = {}

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            phone_number = show_phone(args, contacts)
            if phone_number:
                print(phone_number)

        elif command == "all":
            show_all(contacts)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
