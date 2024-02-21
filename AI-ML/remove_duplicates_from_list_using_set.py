l = []
i = int(input("Enter the number of values to be entered: "))
print("Enter the values in the list:")

for a in range(i):
    new_entry = int(input())
    l.append(new_entry)


new_list=list(set(l))

print(new_list)