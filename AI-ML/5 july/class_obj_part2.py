class demo:
    n=1
    def demofunction(self):
        print("Hiii")
        print(id(self))

d=demo()
print(d.n)
d.demofunction()


d1=demo()
d1.demofunction()

print(id(d1))#same as self
print(id(d))#was same as self   now is not




'''
method:present inside the class and only object of the class can call this
function: general

'''



