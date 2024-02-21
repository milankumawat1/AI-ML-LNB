i = input("Enter the string")
c={}

for char in i:
    if char in c:
        c[char] +=1
    else:
        c[char] =1

print(c)