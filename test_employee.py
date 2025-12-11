from employee import employee_details
def test_employee_details():
    output=(
        "Employee_Name:Alice\n"
        "Employee_ID:E1001\n"
        "Department:IT\n"
        "Salary:55000"
    )
    assert employee_details("Alice","E1001","IT",55000) == output
