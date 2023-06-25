from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.wcxuzba.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

# Insert Richard's document
richard = {
    "student_id": 1007,
    "first_name": "Richard",
    "last_name": "Africain"
}

richard_student_id = students.insert_one(richard).inserted_id

print(richard_student_id)

# Insert Jean's document
jean = {
    "student_id": 1008,
    "first_name": "Jean",
    "last_name": "Africain"
}

jean_student_id = students.insert_one(jean).inserted_id

print(jean_student_id)

# Insert John's document
john = {
    "student_id": 1009,
    "first_name": "John",
    "last_name": "Doe"
}

john_student_id = students.insert_one(john).inserted_id

print(john_student_id)
