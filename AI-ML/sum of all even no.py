# l=[]
# a=0
# i=int(input("enter the no of values to be entered"))
# print('Enter the values in list')

# while a<i:
#     new_entry=int(input())
#     l.append(new_entry)
#     a+=1

# c=0
# d=0
# for j in l:
#     b=l[d]%2
#     if b==0:
#         c=c+l[d]
#     d+=1    

# print(c)



l = []
i = int(input("Enter the number of values to be entered: "))
print("Enter the values in the list:")

for a in range(i):
    new_entry = int(input())
    l.append(new_entry)

c = 0
for a in l:
    if a % 2 == 0:
        c += a

print(c) 
