class Employee:

    def __init__(self, employee_id, name, email, department, designation, joining_date):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.designation = designation
        self.joining_date = joining_date

    def __str__(self):
        return (
            f"\nEmployee ID : {self.employee_id}\n"
            f"Name         : {self.name}\n"
            f"Email        : {self.email}\n"
            f"Department   : {self.department}\n"
            f"Designation  : {self.designation}\n"
            f"Joining Date : {self.joining_date}\n"
        )