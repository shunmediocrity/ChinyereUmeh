import sqlite3

# Connect to database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Step 1: Create Departments Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
)
""")

# Step 2: Create Employees Table with Foreign Key
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department_id INTEGER,
    salary REAL,
    FOREIGN KEY (department_id) REFERENCES departments(id) ON DELETE CASCADE
)
""")

conn.commit()
print("Database schema updated with relational tables!")

# Step 3: Insert Departments
departments = [("HR",), ("IT",), ("Finance",), ("Marketing",)]
cursor.executemany("INSERT OR IGNORE INTO departments (name) VALUES (?)", departments)
conn.commit()
print("Departments inserted successfully!")

# Step 4: Fetch department IDs
cursor.execute("SELECT id, name FROM departments")
departments_dict = {name: dept_id for dept_id, name in cursor.fetchall()}

# Step 5: Insert Employees with Department References
employees = [
    ("Alice", 30, departments_dict["HR"], 50000),
    ("Bob", 25, departments_dict["IT"], 60000),
    ("Charlie", 35, departments_dict["Finance"], 70000),
    ("David", 28, departments_dict["Marketing"], 55000),
    ("Eve", 40, departments_dict["IT"], 80000)
]

cursor.executemany("INSERT INTO employees (name, age, department_id, salary) VALUES (?, ?, ?, ?)", employees)
conn.commit()
print("Employees inserted successfully!")

# Step 6: Retrieve Employee Data with Departments
cursor.execute("""
SELECT employees.id, employees.name, employees.age, departments.name, employees.salary
FROM employees
JOIN departments ON employees.department_id = departments.id
""")

employees_with_departments = cursor.fetchall()

print("\nEmployee Details with Department Names:")
for emp in employees_with_departments:
    print(emp)

conn.close()