class Employee:
    def __init__(self, name, salary, phone_number, start_date):
        self.name = name
        self.salary = salary
        self.phone_number = phone_number
        self.start_date = start_date

    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)

employee_two = Employee("Fran", 80000, "342342", "1st June 2021")
print()