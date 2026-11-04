import re

def validate_student(name, email, department):
    if not name.strip():
        return False, "Name is required"

    if not re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", email):
        return False, "Enter a valid email address"

    if not department.strip():
        return False, "Department is required"

    return True, "Valid student details"