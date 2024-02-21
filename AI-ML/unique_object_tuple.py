

t=()

i = int(input("Enter the number of values to be entered: "))
print("Enter the values in the tuple:")

for a in range(i):
    new_entry = int(input())
    t += (new_entry,)
c={}

for char in t:
    if char in c:
        print("False")
        exit()
    else:
        c[char]=1


print("True")