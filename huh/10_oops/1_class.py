# class is  a blueprint or a template. Eg. Form for an Exam that contains name, age , electives, father's name etc

# object: Specific instance created from the template (class) . for eg:- Form which contains the data for John Doe 

class Employee:
    company = "HP"

    def get_salary(self): # self referred as the object of the class which is being created # self is important here coz self is a way for reference of the class which is being created
        return 34000
    


e = Employee() # an object of class employee is created here
print(e.get_salary()) # Employee e's get salary method is called

e2 = Employee()
print(e2.get_salary())
print(e2.company)