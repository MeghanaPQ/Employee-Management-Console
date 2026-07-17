import re

def validate_employee_id(employee_id):
    return employee_id.strip() != ""

def validate_name(name):
    return name.strip() != ""

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None