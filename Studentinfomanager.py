# Initialize empty lists and dictionary to store student's information
students_list = []
students_dict = {}

# Add student information
name = input("Enter student's name: ")
age = input("Enter student's age: ")
grade = input("Enter student's grade: ")
students_list.append(name)
students_dict[name] = {"age": age, "grade": grade}
print("Student information added successfully!")
print(students_dict.items())

# Search for a student by name 
search_name = input("Enter the name of the student: ")
if search_name in students_list:
    print(f"student found! Author: {students_dict[search_name]}")
else:
    print("student not found!")

# Remove a student
remove_name = input("Enter the name of the student to remove or simply enter to skip: ")
if remove_name in students_list:
    del students_dict(remove_name)
    students_list.remove(remove_name)
    print("Student removed sucessfully!")
else:
    print("Student not found!")