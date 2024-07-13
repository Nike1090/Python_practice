class Person():
    def __init__(self, firstName, lastName) -> None:
        self.firstName = firstName
        self.lastName = lastName

    def full_name(self):
        return self.firstName + " " + self.lastName

class Employee(Person):
    def __init__(self, firstName, lastName, role, salary) -> None:
        super().__init__(firstName, lastName)
        self.role = role
        self.salary = salary

    def employee_details(self):
        return f'Employee Details: {self.full_name()}' \
        f' role: {self.role}' \
        f' Salary: {self.salary}'


p1 = Person("max", "Holloway")
print(p1.full_name())

e1 = Employee("Rashi", "stephan", "software analyst", 320000)
print(e1.employee_details())

        
    
