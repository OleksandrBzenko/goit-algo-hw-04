def parse_input(user_input):
    parts = user_input.strip().split()
    cmd = parts[0].lower() if parts else ""
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Error: Please provide both name and phone number."
    
def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Error: Contact not found."
    except ValueError:
        return "Error: Please provide both name and phone number."
        
def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"{name} {contacts[name]}"
        else:
            return "Error: Contact not found."
    except IndexError:
        return "Error: Please provide a name."
    
def show_all(contacts):
    if  contacts:
        result = ["All contacts:"]
        for name, phone in contacts.items():
            result.append(f"{name}: {phone}")
        return "\n".join(result)
    else:
        return "No contacts found."




def main():
    contacts = {}
    print("Welcome to the assistanst bot!")
    
    while True:
        try:
            user_input = input("Enter a command:")
            command, args = parse_input(user_input)
        
            if command in ["close", "exit"]:
                print("Good bye!")
                break

            elif command == "hello":
                print("Hello! How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            elif command == "": 
                print("Please enter a command.")
            else:
                print("Invalid command.")
        except Exception as e:
            print(f"An error occured: {e}")


if __name__ == "__main__":
    main()