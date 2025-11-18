import sqlite3

# Connect to database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create employees table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary REAL
)
""")
conn.commit()

# Functions
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    cursor.execute("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)",
                   (name, age, department, salary))
    conn.commit()
    print(f"\nEmployee {name} added successfully!\n")

def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    if not employees:
        print("\nNo employees found.\n")
    else:
        print("\nEmployee List:")
        for emp in employees:
            print(emp)
    print()

def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))

    cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    employee = cursor.fetchone()

    if not employee:
        print("\nEmployee not found!\n")
        return

    print("\nUpdating Employee:", employee)

    name = input("Enter new name (or press Enter to keep the same): ") or employee[1]
    age = input("Enter new age (or press Enter to keep the same): ")
    department = input("Enter new department (or press Enter to keep the same): ") or employee[3]
    salary = input("Enter new salary (or press Enter to keep the same): ")

    age = int(age) if age else employee[2]
    salary = float(salary) if salary else employee[4]

    cursor.execute("UPDATE employees SET name = ?, age = ?, department = ?, salary = ? WHERE id = ?",
                   (name, age, department, salary, emp_id))
    conn.commit()
    print(f"\nEmployee ID {emp_id} updated successfully!\n")

def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
    employee = cursor.fetchone()

    if not employee:
        print("\nEmployee not found!\n")
        return

    confirm = input(f"Are you sure you want to delete {employee[1]}? (yes/no): ").lower()
    if confirm == "yes":
        cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
        conn.commit()
        print(f"\nEmployee ID {emp_id} deleted successfully!\n")
    else:
        print("\nDelete action canceled.\n")

# Menu function
def menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("\nExiting... Goodbye!")
            conn.close()
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.\n")

# Run the menu
menu()