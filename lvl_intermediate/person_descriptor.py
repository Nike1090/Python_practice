class Person:
    def __init__(self, firstName, lastName, Age, Address) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.Age = Age
        self.Address = Address

    def Persons_info(self):
        print(f"Full Name: {self.firstName} Last Name: {self.lastName} age: {self.Age} Address: {self.Address}")

ram = Person("ram", "varma",  34, "dexters st")
ram.Persons_info()