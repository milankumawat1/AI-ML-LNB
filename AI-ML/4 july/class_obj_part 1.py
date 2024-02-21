'''
class:
    is a blueprint or template that defines the structure and behavior of object
    class is a collection of data member and member function
    a class define the attribute (data) and method(function) that the object of that class can have


Object:
    is an instance (specific occurance or realization) of the class
    it is created based on the blueprint or template provided by the class
    

self:
    it contain the object of the class
'''


class demo:
    n=1
    def demofunction(self):
        print("Hiii")



d=demo()
print(d.n)
print(d.demofunction())





