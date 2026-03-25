# 🔥 PART 2 — DICTIONARIES

# ✅ What is Dictionary?

# Dictionary = key-value pair

# 👉 Ordered (Python 3.7+)
# 👉 Mutable
# 👉 Keys unique होती हैं
# 👉 { key : value }

# ⭐ 1. Create Dictionary

student = {
    "name": "Shashi",
    "age": 21,
    "city": "Bhopal"
}

# ⭐ 2. Access Values
print(student["age"])
print(student.get("name"))


# ⭐ 3. Modify Dictionary
student["age"] = 24
student["college"] = "SIRTE"

print(student)


#⭐ 4. Remove Items
# student.pop("age")

# del student["city"]


# ⭐ 5. Loop through Dictionary
for key in student:
    print(key, student[key])

# OR
for key, value in student.items():
    print(key, value)


# ⭐ 6. Dictionary Methods
print(student.keys())
print(student.values())
print(student.items())


# ⭐ 7. Nested Dictionary (Advanced)
students = {
    1 : {"name": "Amit", "age": 21},
    2 : {"name": "Sumit", "age": 18}
}
print(students[1]["name"])



# ⭐ 8. Dictionary Comprehension (Very Important)
squares = {x: x*x for x in range(1,6)}
print(squares)