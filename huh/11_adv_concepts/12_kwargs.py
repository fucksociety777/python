def marks(**kwargs):
    # kwargs is a dictionary with all the key value pairs which were passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")
        
marks(goku=20, gohan=15, rikin=11, vegeta=19)