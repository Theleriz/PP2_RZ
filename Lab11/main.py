import psycopg2

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
    );
""")
print("Table was created or already exist.")


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter number: ")
    cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    print("Record was added.")


def update_data():
    field = input("What you want? (name/phone): ").lower()
    target = input("Enter current data: ")
    new_value = input("New value: ")

    if field == "name":
        cursor.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_value, target))
    elif field == "phone":
        cursor.execute("UPDATE PhoneBook SET phone = %s WHERE phone = %s", (new_value, target))
    print("Success.")


def query_data():
    print("Choice option:\n 1 - all records\n 2 - by name\n 3 - by number\n 4 - by id segment\n 5 - by pattern")
    choice = input("Choice option: ")

    if choice == "1":
        cursor.execute("SELECT * FROM PhoneBook ORDER BY id")
    elif choice == "2":
        name = input("Enter name: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
    elif choice == "3":
        phone = input("Enter number: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    elif choice == "4":
        id_start = input("Enter start id: ")
        id_end = input("Enter end id id: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE id >= %s AND id <= %s", (id_start, id_end))
    elif choice == "5":
        pattern = input("Write pattern: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE name LIKE %s OR phone LIKE %s", (f"%{pattern}%", f"%{pattern}"))
    else:
        print("Bad option.")

    results = cursor.fetchall()
    for row in results:
        print(row)


def query_with_pg():
    limit = 5
    page = int(input("Enter page: "))
    offset = (page - 1) * limit
    cursor.execute("SELECT * FROM PhoneBook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    results = cursor.fetchall()

    if results:
        print(f"\nResult (page {page}):")
        for row in results:
            print(row)
    else:
        print("No data.")


def delete_data():
    print("Delete by:\n name\nnumber")
    choice = input("Enter option: ")

    if choice == "name":
        name = input("Enter name: ")
        cursor.execute("DELETE FROM PhoneBook WHERE name = %s", (name))
    elif choice == "number":
        phone = input("Enter number: ")
        cursor.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone))
        return



def reset_table():
    confirm = input("Reset table? (yes/no): ").lower()
    if confirm == "yes":
        cursor.execute("DROP TABLE IF EXISTS PhoneBook;")
        cursor.execute("""
            CREATE TABLE PhoneBook (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                phone VARCHAR(20) NOT NULL
            );
        """)
        print("Table was reseted.")
    else:
        print("Operation was cancelled.")


def insert_many_users():
    lst_user = []
    lst_number = []
    size = int(input("Number of users: "))
    print("\n")

    for i in range(size):
        user = input(f"Name of {i + 1} user: ")
        number = input(f"Number of {user}: ")
        lst_user.append(user)
        lst_number.append(number)

    for i in range(size):
        
        cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (lst_user[i], lst_number[i]))
        print(f"User {lst_user[i]} is inserted into database")
        



while True:
    print("\n  Choose option:")
    print("1. New record")
    print("2. Add many records")
    print("3. Update record")
    print("4. Show records")
    print("5. Delete record")
    print("6. Reset table")
    print("7. Show with pagination")
    print("8. Quite")

    option = input("Choice option: ")

    if option == "1":
        insert_from_console()
    elif option == "2":
        insert_many_users()
    elif option == "3":
        update_data()
    elif option == "4":
        query_data()
    elif option == "5":
        delete_data()
    elif option == "6":
        reset_table()
    elif option == "7":
        query_with_pg()
    elif option == "8":
        break
