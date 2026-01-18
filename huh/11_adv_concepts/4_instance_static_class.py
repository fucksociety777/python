class Employee:
    company = "HP"
    def __init__(self,  name , salary):
        self.name = name 
        self.salary = salary 
        
      # INstance method (default)  
    def print_info(self):
        info =  f"The name is {self.name} and the salary is {self.salary}"
        print(info)
        
     # this static method is a method which doesn't require self
    @staticmethod 
    def sum(a , b):
        return a + b        
    # class methods is a decorator
    @classmethod
    def print_company(cls):
        print(cls.company)
        
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        
        
e1 = Employee("Goku", 10000)
e2 = Employee("Gohan", 20000)
# print(Employee.company) # this will print(output) HP
# print(Employee.name) # this will throw an error
 
# e1.print_info()
# e2.print_info()

# print(e2.sum(3, 30))


e1.print_company()
e1.change_company("Acer")
e1.print_company()
print(Employee.company)