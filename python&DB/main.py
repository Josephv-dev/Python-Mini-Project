import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Read and execute schema.sql setup
with open("schema.sql", "r") as sql_file:
    sql_script = sql_file.read()

cursor.executescript(sql_script)
conn.commit()


# Check if any user exists
def user_exists():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0] > 0


def register():
    print("\n=== REGISTER ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )
        conn.commit()
        print("Registration successful\n")
    except sqlite3.IntegrityError:
        print("Username already exists\n")


def login():
    print("\n=== LOGIN ===")
    username = input("Username: ")
    password = input("Password: ")

    cursor.execute(
        "SELECT id FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    if user:
        print("Login successful\n")
        return user[0]
    else:
        print("Invalid login\n")
        return None


def add_expense(user_id):
    amount = float(input("Amount: "))
    date = input("Date: ")
    description = input("Description: ")
    category = input("Category: ")
    payment_method = input("Payment method: ")
    recurring = input("Recurring (Yes/No): ")

    cursor.execute("""
    INSERT INTO expenses
    (user_id,amount,date,description,category,payment_method,recurring)
    VALUES(?,?,?,?,?,?,?)
    """, (user_id, amount, date, description, category, payment_method, recurring))

    conn.commit()
    print("Expense added\n")


def view_expenses(user_id):
    cursor.execute(
        "SELECT amount,date,description,category,payment_method FROM expenses WHERE user_id=?",
        (user_id,)
    )

    rows = cursor.fetchall()

    print("\n=== YOUR EXPENSES ===")
    for row in rows:
        print(row)


# MAIN PROGRAM

if not user_exists():
    print("No users found. Please register first.")
    register()

while True:
    print("\n1 Login")
    print("2 Register")
    print("3 Exit")

    choice = input("Choose option: ")

    if choice == "1":
        user_id = login()

        if user_id:
            while True:
                print("\n1 Add Expense")
                print("2 View Expenses")
                print("3 Logout")

                option = input("Select: ")

                if option == "1":
                    add_expense(user_id)

                elif option == "2":
                    view_expenses(user_id)

                elif option == "3":
                    break

    elif choice == "2":
        register()

    elif choice == "3":
        break

conn.close()