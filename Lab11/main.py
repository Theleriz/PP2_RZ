import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "1"
db_name = "task1"

try:
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
    print("Таблица создана или уже существует")

 
    def insert_from_console():
        name = input("Enter name: ")
        phone = input("Enter number: ")
        cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
        print("Record was added.")

    def update_data():
        field = input("What you want? (name/phone): ").strip().lower()
        target = input("Enter current data: ").strip()
        new_value = input("New value: ").strip()

        if field == "name":
            cursor.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_value, target))
        elif field == "phone":
            cursor.execute("UPDATE PhoneBook SET phone = %s WHERE phone = %s", (new_value, target))
        print("Sucess.")




    def query_data():
        print("Choice option:\n 1 - all records\n 2 - by name\n 3 - by number\n 4 - by id segment\n 5 - by pattern")
        choice = input("Введите номер выбора: ")

        if choice == "1":
            cursor.execute("SELECT * FROM PhoneBook ORDER BY id")
        elif choice == "2":
            name = input("Введите имя: ")
            cursor.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
        elif choice == "3":
            phone = input("Введите номер телефона: ")
            cursor.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
        elif choice == "4":
            id_start= input("Введите начало id: ")
            id_end= input("Введите конец id: ")

            cursor.execute("SELECT * FROM PhoneBook WHERE id >= %s AND id <= %s", (id_start, id_end))
        elif choice == "5":
                pattern = input("Write pattern: ")
                cursor.execute("SELECT * FROM PhoneBook WHERE name LIKE %s OR phone LIKE %s", (f"%{pattern}%", f"%{pattern}%"))
    

            
            
        else:
            print("Неверный выбор.")
            return

        results = cursor.fetchall()
        for row in results:
            print(row)

    def query_with_pagination():
        
        limit = 5
        page = int(input("Номер страницы: "))

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
        print("Delete by:\n1 - name\n2 - number")
        choice = input("Enter option: ")

        if choice == "1":
            name = input("Enter name: ")
            cursor.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
        elif choice == "2":
            phone = input("Enter number: ")
            cursor.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))
            return

        
        cursor.execute("SELECT setval(pg_get_serial_sequence('PhoneBook', 'id'), MAX(id)) FROM PhoneBook;")
        

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
            print("operation was cancled")

        
    def insert_many_users():
        lst_user = []
        lst_number = []
        size = int(input("number of users: "))
        print("\n")

        for i in range(size):
            user = input(f"Name of {i+1} user: ")
            number = input(f"Number of{user}: ")
            lst_user.append(user)
            lst_number.append(number)

        
        for i in range(size):
            try:
                cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (lst_user[i], lst_number[i]))
                print(f"User {lst_user[i]} is inserted to database")

            except Exception as e:
                print(f"Error of user{lst_user[i]}, {e}")



        
        
        
        



    # Простой интерфейс
    while True:
        print("\n   Меню PhoneBook:")
        print("1. New record")
        print("2. Add many records")
        print("3. Update record")
        print("4. Show records")
        print("5. Delete record")
        print("6. Reset table")
        print("7. Quite")
        print("8. Show with pagination")

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
            break
        elif option == "8":
            query_with_pagination()
        

except Exception as e:
    print("   No connection with database:", e)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("   End session.")
