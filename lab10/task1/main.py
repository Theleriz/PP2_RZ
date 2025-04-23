import psycopg2
import csv

host = "127.0.0.1"
user = "postgres"
password = "88662244"
db_name = "demodb"

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)
connection.autocommit = True
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL
);""")
print("Table was created or already exists.")


def InsertFromConsole():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    
    cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    print("Record added successfully.")

def InsertFromCSV():
    with open('highscores.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, score = row
        cursor.execute("INSERT INTO highscores (name, score) VALUES (%s, %s)", (name, int(score)))


def UpdateData():
    field = input("Which field do you want to update? (name/phone): ").lower()
    target = input("Enter the current value (name or phone number): ")
    new_value = input("Enter the new value: ")

    if field == "name":
        cursor.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_value, target))
    elif field == "phone":
        cursor.execute("UPDATE PhoneBook SET phone = %s WHERE phone = %s", (new_value, target))
    else:
        print("Invalid field.")
        return
    print("Data updated successfully.")


def QueryData():
    print("Select a filter:\n1 - All records\n2 - By name\n3 - By phone number")
    choice = input("Enter your choice number: ")
    if choice == "1":
        cursor.execute("SELECT * FROM PhoneBook")
    elif choice == "2":
        name = input("Enter name: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
    elif choice == "3":
        phone = input("Enter phone number: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    else:
        print("Invalid choice.")
        return

    results = cursor.fetchall()
    for row in results:
        print(row)


def DeleteData():
    print("Delete by:\nName\nPhone number").lower()
    option = input("Enter your choice number: ")

    if option == "name":
        name = input("Enter name: ")
        cursor.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    elif option == "phone number":
        phone = input("Enter phone number: ")
        cursor.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
    else:
        print("Invalid choice.")
        return

    print("Data deleted successfully.")


def TableReset():
    confirm = input("You sure? (yes/no): ").lower()
    if confirm == "yes":
        cursor.execute("DROP TABLE IF EXISTS PhoneBook;")
        cursor.execute("""
            CREATE TABLE PhoneBook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                phone VARCHAR(20) NOT NULL
            );""")
        print("Table has been reset and recreated.")
    else:
        print("Cancelled.")


while True:
    print("\nPhoneBook Menu:")
    print("1. Add a record")
    print("2. Update a record")
    print("3. View records")
    print("4. Delete a record")
    print("5. Reset table")
    print("6. Exit")

    option = input("Choose an action: ")

    if option == "1":
        print("Choose option:\n1. Insert from console.\n2. Insert from csv file.")
        choice = input()
        if choice == "1":
            InsertFromConsole()
        if choice == "2":
            InsertFromCSV()
    elif option == "2":
        UpdateData()
    elif option == "3":
        QueryData()
    elif option == "4":
        DeleteData()
    elif option == "5":
        TableReset()
    elif option == "6":
        break
    else:
        print("Invalid input.")
