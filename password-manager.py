class PasswordEntry:
    def __init__(self, service, username, password):
        self.service = service
        self.username = username
        self.password = password

    def show_details(self):
        if len(self.password) > 4:
            hidden_password = self.password[:3] + "*" * (len(self.password) - 3)
        else:
            hidden_password = "****"

        print(f"Service: {self.service} | Username: {self.username} | Password: {hidden_password}")

class PasswordManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def show_all_entries(self):
        for entry in self.entries:
            entry.show_details()

manager = PasswordManager()
password1 = PasswordEntry("Google", "Tomik123", "917302")
password2 = PasswordEntry("Telegram", "Tomik123", "917302")
manager.add_entry(password1)
manager.add_entry(password2)

while True:
    print("Welcome to Password Manager!")
    print("1. Add a new password")
    print("2. Show all passwords")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        service = input("Enter service: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        manager.add_entry(PasswordEntry(service, username, password))

    elif choice == 2:
        manager.show_all_entries()

    elif choice == 3:
        print("Thank you for using Password Manager!")
        break




