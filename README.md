# Employee Management Console Application

## Description

The Employee Management Console Application is a Python-based console application developed as part of the **Coding Best Practices for Beginners** assignment.

The application allows users to manage employee records through a menu-driven interface. It supports adding, viewing, searching, updating, deleting, sorting, and filtering employee records. Employee data is stored in a JSON file so that records are preserved even after the application is closed.

---

# Features Implemented

## Core Features

- Add Employee
- View All Employees
- Search Employee by Employee ID
- Update Employee Details
- Delete Employee
- Exit Application

---

## Bonus Features

- Sort Employees by Name
- Filter Employees by Department
- Prevent Duplicate Employee IDs
- Save Employee Records in JSON File
- Automatically Load Employee Records from JSON File

---

# Employee Details

Each employee record contains:

- Employee ID
- Name
- Email
- Department
- Designation
- Joining Date

---

# Validation

The following validations are implemented:

- Employee ID cannot be empty
- Employee ID must be unique
- Name cannot be empty
- Email format validation
- Graceful handling of invalid input

---

# Best Practices Followed

The project follows clean coding principles:

- Meaningful class names
- Meaningful variable names
- Meaningful method names
- Proper indentation
- Modular code structure
- Separate business logic from user interaction
- Reusable methods
- Input validation
- Error handling
- Clean and readable code

---

# Project Structure

```
EmployeeManagement/
│
├── employee.py
├── employee_service.py
├── validation.py
├── main.py
├── employee.json
├── employees.json
├── requirements.txt
├── README.md
└── .vscode/
```

---

# Technologies Used

- Python 3
- JSON
- Object-Oriented Programming (OOP)
- Visual Studio Code

---

# How to Run

## Step 1

Install Python 3 on your system.

## Step 2

Download or clone the repository.

```
git clone https://github.com/MeghanaPQ/Employee-Management-Console.git
```

## Step 3

Open the project folder in Visual Studio Code.

## Step 4

Open the terminal.

## Step 5

Run the application.

```
python main.py
```

---

# Menu

```
===== Employee Management System =====

1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Sort Employees by Name
7. Filter Employees by Department
8. Exit
```

---

# Sample Output

```
===== Employee List =====

Employee ID : 101
Name        : Meghana
Email       : meghana08@gmail.com
Department  : AI-ML
Designation : Intern
Joining Date: 01-07-2026
```

---

# Files Description

### employee.py

Contains the Employee model class.

### employee_service.py

Contains all business logic including CRUD operations, sorting, filtering, and JSON file handling.

### validation.py

Contains validation methods for Employee ID, Name, and Email.

### main.py

Contains the menu-driven console interface.

### employees.json

Stores employee records permanently.

### requirements.txt

Lists project dependencies.

---

# Future Improvements

- Connect with or MySQL database
- Add Login Authentication
- Develop REST APIs using Flask or FastAPI
- Add Unit Testing

---

# Author

**Meghana KesamReddy**

Developed as part of the **Coding Best Practices for Beginners** assignment.
