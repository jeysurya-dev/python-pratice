class Employee:
    def __init__(self, name, job_title, salary):
        self.name = name
        self.job_title = job_title
        self.salary = salary

    def calculate_salary(self):
        return self.salary * 12

    def update_salary(self, new_salary):
        self.salary = new_salary

# Example usage
employee1 = Employee("John Doe", "Software Engineer", 5000)

# Calculate annual salary
annual_salary = employee1.calculate_annual_salary()
print(f"Annual Salary of {employee1.name}: {salary}")

# Update salary
employee1.update_salary(5500)
print(f"Updated Salary of {employee1.name}: {employee1.salary}")
