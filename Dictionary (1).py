students = {
    101: "Rahul",
    102: "Anita",
    103: "Vikas",
    104: "Sneha",
    105: "Arjun"
}

students[106] = "Kiran"
print("After Adding:", students)

students[103] = "Vikram"
print("After Updating:", students)


print("Student with ID 102:", students[102])

student_details = {
    101: {"name": "Rahul", "age": 20},
    102: {"name": "Anita", "age": 21},
    103: {"name": "Vikram", "age": 22}
}


print("Name of Student 101:", student_details[101]["name"])
print("Age of Student 102:", student_details[102]["age"])


print("Keys:", list(students.keys()))


# 1.7 Delete a value from a dictionary
# del students[105]
# print("After Deleting:", students)
