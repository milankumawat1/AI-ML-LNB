'''
Data types:

numeric
    int
    float
    complex no




sequence
    string
    list
    tuple


unordered
    dictionary
    set


'''


#Complex No.
a=1+4j
print(type(a))

print(a)

r=a.real
i=a.imag
print("Real:",r,"Imaginary:",i)



#string

s="hii how are you?"
print(s,"is of",type(s))



'''
List:

is an unordered sequence of item
it is one of the most used datatype in python and is very flexible
it is mutable
denoted by[]
'''

l=[1,2,3,4.1,5.6,'LnB']
print(l)
print(type(l))

print(l[5])

l[2]=3.3
print(l)


'''
Tuple:
    is an ordered of item same as a list
    it is defined within ()
    it is immutable
    need to have more than one value
'''

t={1,2.2,'lnb'}

print(t)
print(type(t))
#need to pass more than 1 value
t1=(1)
print(t1)
print(type(t1))#int





print(t[1])

