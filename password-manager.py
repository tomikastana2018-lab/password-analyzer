import psycopg2
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
        self.connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password=""
        )
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id SERIAL PRIMARY KEY,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def add_entry(self, entry):
        self.cursor.execute("""
        INSERT INTO passwords (service, username, password)
        VALUES (%s, %s, %s)
        """,(entry.service, entry.username, entry.password))
        self.connection.commit()
        print("Password Added!")

    def show_all_entries(self):
        self.cursor.execute("SELECT * FROM passwords")
        rows = self.cursor.fetchall()

        if not rows:
            print("No entries found!")
            return
        print("Your Passwords:")
        for row in rows:
            entry_id, service, username, password = row

            if len(password) > 4:
                hidden_password = password[:3] + "*" * (len(password) - 3)
            else:
                hidden_password = "****"
            print(f"ID: {entry_id} | Service: {service} | Username: {username} | Password: {hidden_password}")

manager = PasswordManager()
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

    elif choice == 2:
        manager.show_all_entries()

    elif choice == 3:
        print("Thank you for using Password Manager!")
        break