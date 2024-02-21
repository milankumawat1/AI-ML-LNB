employees={}
class HR_DEP:
    def __init__(self,hres,**kwargs):
        print("HR department")
        super().__init__(**kwargs)
        self.hres=hres
        
    def add_employee(self,name,salary):
        employees[name]=salary
    
    def print_employee(self):
        print(employees)

class FINANCE_DEP:
    def __init__(self,fres,**kwargs):
        print("FINANCE department")
        super().__init__(**kwargs)
        self.fres=fres
        employees={}
    def add_employee(self,name,salary):
        employees[name]=salary
    
    def print_employee(self):
        print(employees)


class SALE_DEP:
    def __init__(self,sres,**kwargs):
        print("SALE department")
        super().__init__(**kwargs)
        self.sres=sres
        employees={}
    def add_employee(self,name,salary):
        employees[name]=salary
    
    def print_employee(self):
        print(employees)
    

class manager(FINANCE_DEP,SALE_DEP,HR_DEP):
    def __init__(self,f,s,h):
        print("All department are as follows")
        super().__init__(fres=f,sres=s,hres=h)
        # super(HR_DEP).__init__()
        # super(FINANCE_DEP,self).__init__()
    def add_employee(self, department, name, salary):
        if department == "HR":
            HR_DEP.add_employee(self,name, salary)
        elif department == "FINANCE":
            FINANCE_DEP.add_employee(self,name, salary)
        elif department == "SALES":
            SALE_DEP.add_employee(self,name, salary)

    def print_employees(self):
        HR_DEP.print_employee(self)
        FINANCE_DEP.print_employee(self)
        SALE_DEP.print_employee(self)
        # self.fres.print_employee()
        # self.sres.print_employee()

m=manager('FINANCE','SALE','HR')
print("**********************************")
e_name = input("Enter the name of the employee: ")
e_salary = float(input("Enter the salary of the employee: "))
department = input("Enter the department (HR, FINANCE, or SALES): ")

m.add_employee(department, e_name, e_salary)

print("**********************************")
m.print_employees()

