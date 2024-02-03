def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return 'error: you must input(add "username" "phone")'

def change_phone(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Phone number for '{name}' changed."
        else:
            return f"Contact {name} not found."
    except ValueError:
        return 'error: you must input (change "username" "phone") or no contacts'

def show_all(contacts):
    if not contacts:
        return 'No contacts available, you need to (add "username" "phone")'
    else:
        result = ''
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()

def get_phone(args, contacts):
    try:
        name, = args
        phone = contacts.get(name)
        if phone:
            return f"Phone number for '{name}': {phone}"
        else:
            return f"Contact {name} not found."
    except ValueError:
        return 'error: you must input (phone "username")'

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()