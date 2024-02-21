'''
It allows you to define a new class based on existing class as base or 
new class is called derived class
proper utilization of memory

'''


'''
class a():
    def DisplayA(self):
        print("I am A class")

class b():
    def DisplayB(self):
        print("I am B class")

class c(a,b):
    def Display(self):
        print("I am C class")



c1=c()
c1.DisplayA()
c1.DisplayB()
c1.Display()

A=a()
A.DisplayA()


'''

'''
class base1():
    def display1(self):
        print('Hi i am from base1 class')

class base2(base1):
    def display2(self):
        print('Hi i am from base 2 class')


class base3(base2):
    def display3(self):
        print("hi i am from base 3 class")

b=base3()
b.display1()
b.display2()
b.display3()

'''

# class Employee:
#     def __init__(self,name,id):
        
#         self.name=name
#         self.id=id
#     def display_info(self):
#         print("Employee name:",self.name)
#         print("Employee id:",self.id)
        
# class RegularEmployee(Employee):
#     def __init__(self,responsibility):
#         self.responsibility=responsibility
#     def display_info(self):
#         print("Responsibility:",self.responsibility)

# class Manager(RegularEmployee):
#     def __init__(self,department):
#         self.department=department
#     def display_info(self):
#         print("Department:",self.department)
       
              
# e=Employee('Randhir',9)
# r=RegularEmployee('Regular')
# m=Manager('HR')
# m.display_info()


# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     def display_info(self):
#         print("Name:", self.name)
#         print("Id:", self.id)


# class RegularEmployee(Employee):
#     def __init__(self,responsibility):
#         super().__init__(name, id)
#         self.responsibility = responsibility


# class Manager(RegularEmployee):
#     def __init__(self, name, id, responsibility, department):
#         super().__init__(name, id, responsibility)
#         self.department = department

#     def display_info(self):
#         super().display_info()
#         print("Responsibility:", self.responsibility)
#         print("Department:", self.department)


# e=Employee('Randhir',9)
# r=RegularEmployee('Regular')
# m=Manager('HR')
# m.display_info()




class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        print("Name:", self.name)
        print("Id:", self.id)


class RegularEmployee(Employee):
    def __init__(self, name, id, responsibility):
        super().__init__(name, id)
        self.responsibility = responsibility

    def display_info(self):
        super().display_info()
        print("Responsibility:", self.responsibility)


class Manager(RegularEmployee):
    def __init__(self, name, id, responsibility, department):
        super().__init__(name, id, responsibility)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Department:", self.department)


e = Employee('Randhir', 9)
r = RegularEmployee('John Doe', 10, 'Regular')
m = Manager('Jane Smith', 11, 'Managerial', 'HR')
m.display_info()
