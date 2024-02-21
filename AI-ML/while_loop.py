# n=1

# n1=0
# while n<=10:
#     n1=n
#     print(n)

#     n=n+n1

#     n+=1


#     s=s+n
#     n+=1
# print(s)


#     n1 += n
#     print(n1)
#     n += 1


# x=0
# y=1
# n=1
# while n<=10:
#     c=x+y
#     y=x
#     x=c
#     print(c)
#     n+=1


# fibonacci series
i = int(input('enter the number'))
n = 0
a = 0
print(a)
b = 1
n1 = 0
while n <= i:
    n += 1
    print(b)
    c = a+b
    a = b
    b = c


# factorial

n = int(input('Enter a number'))
s = 1
while n > 0:
    s = s*n
    n -= 1
print(s)
