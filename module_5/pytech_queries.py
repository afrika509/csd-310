from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.wcxuzba.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

# Retrieve all student documents from the students collection
students_list = students.find({})

# Output each student document
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students_list:
    print("Student ID: " + str(student["student_id"]))
    print("First Name: " + student["first_name"])
    print("Last Name: " + student["last_name"])
    print()

# Retrieve a single student document by student_id
student = students.find_one({"student_id": 1007})

# Output the matching student document
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("Student ID: " + str(student["student_id"]))
print("First Name: " + student["first_name"])
print("Last Name: " + student["last_name"])
print()
