students = []

while True:
    i = input('Do you want to enter a record (yes/no)?: ')
    if i == 'no':
        break
    elif i == 'yes':
        name = input("Enter student name: ")
        roll_no = input("Enter student roll number: ")
        percentage = float(input("Enter student percentage: "))
        year = input("Enter student year: ")

        for student in students:
            if student['roll_no'] == roll_no:
                print("Roll number already exists. Please enter a unique roll number.")
                break
        else:
            students.append({
                'name': name,
                'roll_no': roll_no,
                'percentage': percentage,
                'year': year
            })
    else:
        print('Enter a valid answer.')

print("\nStudent Entries:")
for student in students:
    print(f"Name: {student['name']}")
    print(f"Roll No: {student['roll_no']}")
    print(f"Percentage: {student['percentage']}")
    print(f"Year: {student['year']}")
    print()
