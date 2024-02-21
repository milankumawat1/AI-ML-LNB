'''
operators

Arithematic:
+
-
*
/
%
**
//


'''


a=10
b=5

print(a+b)#15
print(a-b)#5
print(a*b)#50
print(a/b)#2
print(a**b)#10000
print(a//b)#2   used for integer divisor
print(a%b)#0





'''
Assignment:

=
+=
-=
/=
//=
%=
*=

'''



a=10
b=5

print(a)
print(b)
a+=1
b+=2


print(a)#a=a+1
print(b)#b=b+2

a/=b# a=11,b=7 a=11/7

print(a)


'''
Comparision:
==
>
<
>=
<=
!=

'''

a=10
b=5
print(a==b)#false
print(a>b)#true
print(a<b)#false
print(a!=b)#true
print(5>=b)#true
print(a<=b)#false



'''
logical operators:

and
or
not

'''

a=19
b=5

print(3<8 and a<=10)
print(3>8 or 4<9)
print(not(3>8 or 4<9))


'''
membership

in
not in

'''

# a=10
# b=10
# print(a in b)  doesnot work on integer type

a='randhir'
print('r' in a)
print('ra' not in a)
print('rha' not in a)

'''
bitwise operator
&
|
^
~

'''

a=4
b=6
print(a&b)

print(bin(a))
print(bin(b))

print(bin(-6))

'''
identity operator
is
is not
'''

a=4
b=5
print(id(a))
print(id(b))
print(a is b)#false
print(a is not b)#true



