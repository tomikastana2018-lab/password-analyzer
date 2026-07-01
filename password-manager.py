import json
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

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

    def save_to_file(self):
        data_to_save = []
        for entry in self.entries:
            entry_dict = {
                "service": entry.service,
                "username": entry.username,
                "password": entry.password
            }
            data_to_save.append(entry_dict)

        with open("passwords.json", "w") as file:
            json.dump(data_to_save, file, indent=4)

    def load_from_file(self):
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
            for item in data:
                entry = PasswordEntry(item["service"], item["username"], item["password"])
                self.entries.append(entry)
        except FileNotFoundError:
            return


manager = PasswordManager()
manager.load_from_file()

master_input = input("Enter Master Password to unlock: ")

if hash_password(master_input) == "8c5b79cdab71169ff689e798250f3157dbf42c81c6c87c62c5d46c2c62febe65":
    print("Access Granted!")
else:
    print("Access Denied!")
    exit()

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
        manager.save_to_file()

    elif choice == 2:
        manager.show_all_entries()

    elif choice == 3:
        print("Thank you for using Password Manager!")
        break





