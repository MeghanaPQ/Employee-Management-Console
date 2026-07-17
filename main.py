from employee_service import EmployeeService

service = EmployeeService()

while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Sort Employees by Name")
    print("7. Filter Employees by Department")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        service.add_employee()

    elif choice == "2":
        service.view_employees()
    elif choice == "3":
        service.search_employee()
    elif choice == "4":
        service.update_employee()
    elif choice == "5":
        service.delete_employee()
    elif choice == "6":
        service.sort_employees_by_name()
    elif choice == "7":
        service.filter_employees_by_department()
    elif choice == "8":
        print("Thank You")
        break

    else:
        print("Invalid Choice")