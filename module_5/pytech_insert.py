from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.wcxuzba.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

# Define the student documents
richard = {
    "student_id": 1007,
    "first_name": "Richard",
    "last_name": "Africain"
}


jean = {
    "student_id": 1008,
    "first_name": "Jean",
    "last_name": "Africain"
}

john = {
    "student_id": 1009,
    "first_name": "John",
    "last_name": "Doe"
}

# Insert each student document into the students collection
student1_id = students.insert_one(richard).inserted_id
student2_id = students.insert_one(jean).inserted_id
student3_id = students.insert_one(john).inserted_id

# Output the added student document IDs
print("Inserted student record Richard Africain into the students collection with document_id " + str(student1_id))
print("Inserted student record Jean Africain into the students collection with document_id " + str(student2_id))
print("Inserted student record John Doe into the students collection with document_id " + str(student3_id))
