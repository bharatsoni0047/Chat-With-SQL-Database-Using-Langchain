import sqlite3 

# connect to sqlite
connection = sqlite3.connect("employees.db")

# create a cursor object to insert record, create table
cursor = connection.cursor()

# create the table
table = '''
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(40),
    salary INT,
    joining_date DATE,
    city VARCHAR(40)
)'''
cursor.execute(table)

# insert some records
cursor.execute("""INSERT INTO employees VALUES (101, 'Rohan Sharma', 'IT', 65000, '2023-04-12', 'Delhi');""")
cursor.execute("""INSERT INTO employees VALUES (102, 'Neha Verma', 'HR', 55000, '2022-10-08', 'Mumbai');""")
cursor.execute("""INSERT INTO employees VALUES (103, 'Amit Patel', 'Finance', 70000, '2023-01-18', 'Ahmedabad');""")
cursor.execute("""INSERT INTO employees VALUES (104, 'Priya Singh', 'Marketing', 60000, '2023-06-21', 'Jaipur');""")
cursor.execute("""INSERT INTO employees VALUES (105, 'Vivek Yadav', 'IT', 72000, '2024-02-03', 'Pune');""")
cursor.execute("""INSERT INTO employees VALUES (106, 'Sneha Gupta', 'Operations', 58000, '2023-09-15', 'Lucknow');""")
cursor.execute("""INSERT INTO employees VALUES (107, 'Karan Mehta', 'Sales', 50000, '2022-12-05', 'Surat');""")

# print records
print("\nInserted records are:- ")
data = cursor.execute("SELECT * FROM employees")

for row in data:
    print(row)

# commit and close
connection.commit()
connection.close()
