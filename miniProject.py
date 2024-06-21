class Employee:
  def __init__(self, name, department):
    self.name = name
    self.department = department
    self.salary = 0
    self.benefits = {}  # Dictionary to store benefits (type, amount)
    self.overtime = 0
    self.banking_details = None
    self.overtime_rate = 10000

  def add_salary(self, amount):
    self.salary = amount

  def add_benefit(self, benefit_type, amount):
    self.benefits[benefit_type] = amount

  def add_overtime(self, hours):
    self.overtime += hours

  def set_banking_details(self, details):
    self.banking_details = details

  def calculate_gross_pay(self):
    # Add logic to calculate gross pay based on salary, overtime pay rate, etc.
    return self.salary + (self.overtime * self.overtime_rate)  # Placeholder

  def generate_payslip(self):
    # Generate payslip with details like name, department, salary, deductions, etc.
    print(f"Employee Name: {self.name}")
    print(f"Department: {self.department}")
    print(f"Gross Pay: {self.calculate_gross_pay()}")
    # Add details for benefits, deductions, net pay, etc.

class Department:
  def __init__(self, name):
    self.name = name
    self.employees = []

  def add_employee(self, employee):
    self.employees.append(employee)


# Sample Usage
employee1 = Employee("John Doe", "Sales")
employee1.add_salary(5000)
employee1.add_benefit("Health Insurance", 100)
employee1.add_overtime(10)
employee1.set_banking_details({"account_number": 1234567890})

department1 = Department("Marketing")
department1.add_employee(employee1)

# Call employee methods to add more employees, benefits, etc.

# Generate payslip
employee1.generate_payslip()

# Add functionalities for viewing employee salary, adding banking details, etc.
