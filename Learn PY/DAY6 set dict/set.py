# ✅ What is a Set?

# Set = unique values का collection

# 👉 Unordered
# 👉 No duplicates
# 👉 Mutable (change कर सकते हैं)
# 👉 {} curly braces

#⭐ 1. Create Set
s = {10,20,30,40}
print(s)

# Duplicate auto remove
s = {1,2,2,3}
print(s)  #{1, 2, 3}



# ⭐ 2. Add & Remove Elements
s.add(45)
s.remove(2)  # error agar element na ho to
s.discard(30) # no error



# ⭐ 3. Set Operations (VERY IMPORTANT)
A = {1,2,3}
B = {3,4,5}

print(A | B)   # union              {1, 2, 3, 4, 5}
print(A & B)   # Intersection       {3}
print(A - B)   # Difference         {1, 2}
print(A ^ B)   # Symmetric Difference {1, 2, 4, 5}


# ⭐ 4. Loop in Set
for x in A:
    print(x)


# ⭐ 5. Convert List → Set (Remove Duplicates)
lst = [1,2,2,3,3,4,5,6,6]
unique = set(lst)
print(unique)