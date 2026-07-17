import json
import validation
from employee import Employee


class EmployeeService:

    def __init__(self):
        self.employees = []
        self.load_from_file()

    def add_employee(self):
        employee_id = input("Enter Employee ID: ")

        if not validation.validate_employee_id(employee_id):
            print("Employee ID cannot be empty.")
            return

        for employee in self.employees:
            if employee.employee_id == employee_id:
                print("Employee ID already exists.")
                return

        name = input("Enter Name: ")

        if not validation.validate_name(name):
            print("Name cannot be empty.")
            return

        email = input("Enter Email: ")

        if not validation.validate_email(email):
            print("Invalid Email.")
            return

        department = input("Enter Department: ")
        designation = input("Enter Designation: ")
        joining_date = input("Enter Joining Date: ")

        employee = Employee(
            employee_id,
            name,
            email,
            department,
            designation,
            joining_date
        )

        self.employees.append(employee)
        self.save_to_file()

        print("Employee added successfully.")

    def view_employees(self):

        if not self.employees:
            print("No employees found.")
            return

        print("\n===== Employee List =====")

        for employee in self.employees:
            print(employee)

    def search_employee(self):
        employee_id = input("Enter Employee ID to search: ")

        for employee in self.employees:
            if employee.employee_id == employee_id:
                print("\n===== Employee Found =====")
                print(employee)
                return

        print("Employee not found.")

    def update_employee(self):
        employee_id = input("Enter Employee ID to update: ")

        for employee in self.employees:
            if employee.employee_id == employee_id:

                name = input(f"Enter New Name ({employee.name}): ")
                if name.strip():
                    employee.name = name

                email = input(f"Enter New Email ({employee.email}): ")
                if email.strip():
                    if validation.validate_email(email):
                        employee.email = email
                    else:
                        print("Invalid Email. Keeping old email.")

                department = input(f"Enter New Department ({employee.department}): ")
                if department.strip():
                    employee.department = department

                designation = input(f"Enter New Designation ({employee.designation}): ")
                if designation.strip():
                    employee.designation = designation

                joining_date = input(f"Enter New Joining Date ({employee.joining_date}): ")
                if joining_date.strip():
                    employee.joining_date = joining_date

                self.save_to_file()

                print("Employee updated successfully.")
                return

        print("Employee not found.")

    def delete_employee(self):
        employee_id = input("Enter Employee ID to delete: ")

        for index, employee in enumerate(self.employees):
            if employee.employee_id == employee_id:
                del self.employees[index]
                self.save_to_file()
                print("Employee deleted successfully.")
                return

        print("Employee not found.")

    def sort_employees_by_name(self):

        if not self.employees:
            print("No employees found.")
            return

        self.employees.sort(key=lambda employee: employee.name.lower())

        print("\n===== Employees Sorted by Name =====")

        for employee in self.employees:
            print(employee)

    def filter_employees_by_department(self):

        department = input("Enter Department: ")

        found = False

        print("\n===== Employees in Department =====")

        for employee in self.employees:

            if employee.department.lower() == department.lower():
                print(employee)
                found = True

        if not found:
            print("No employees found in this department.")

    def save_to_file(self):

        employee_list = []

        for employee in self.employees:

            employee_list.append({
                "employee_id": employee.employee_id,
                "name": employee.name,
                "email": employee.email,
                "department": employee.department,
                "designation": employee.designation,
                "joining_date": employee.joining_date
            })

        with open("employees.json", "w") as file:
            json.dump(employee_list, file, indent=4)

    def load_from_file(self):

        try:

            with open("employees.json", "r") as file:

                employee_list = json.load(file)

                for data in employee_list:

                    employee = Employee(
                        data["employee_id"],
                        data["name"],
                        data["email"],
                        data["department"],
                        data["designation"],
                        data["joining_date"]
                    )

                    self.employees.append(employee)

        except FileNotFoundError:
            pass

        except json.JSONDecodeError:
            pass