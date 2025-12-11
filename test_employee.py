from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Bhimangouda\n"
        "Employee ID: 172\n"
        "Employee Department: IT\n"
        "Employee Salary: 50000"
    )

    result = employee_details("Bhimangouda", "172", "IT", "50000")
    assert result == expected_output
