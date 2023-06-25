from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.wcxuzba.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

# Display all documents in the collection
docs = students.find()

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    print(f"Student ID: {doc['student_id']}")
    print(f"First Name: {doc['first_name']}")
    print(f"Last Name: {doc['last_name']}")
    print()

# Update student_id 1007
students.update_one({"student_id": 1007}, {"$set": {"last_name": "Francois"}})

# Find student_id 1007 after update
updated_doc = students.find_one({"student_id": 1007})

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")

print(f"Student ID: {updated_doc['student_id']}")
print(f"First Name: {updated_doc['first_name']}")
print(f"Last Name: {updated_doc['last_name']}")

print()

print("End of program, press any key to continue...")
