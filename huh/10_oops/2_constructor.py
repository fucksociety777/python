class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary # create and instance attribute of name salary and assign it
        self.name = name
        self.bond = bond

    def get_info(self):
        print(f"The name of the Employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years")

e1 = Employee(34000, "John Doe", 4)
e1.get_info()