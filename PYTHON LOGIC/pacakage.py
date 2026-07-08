import pymongo

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Step 2: Create / Connect to a Database
db = client["school"]

# Step 3: Create / Connect to a Collection
students = db["students"]

# Step 4: Insert one student record
student = {"name": "John", "age": 20, "course": "Python"}
students.insert_one(student)

# Step 5: Read one record
print("One student record:")
print(students.find_one())

# Step 6: Read all records
print("\nAll student records:")
for s in students.find():
    print(s)
