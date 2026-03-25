'''
⭐ PART 2 — TUPLES

Tuple = List जैसा ही, परंतु immutable (change नहीं कर सकते)

👉 Ordered
👉 Unchangeable
👉 Faster than list
👉 Elements → () round brackets में
'''

#🔥 1. Create Tuple
tp = (10, 20, 30)
names = ("shashi", "rahul")

#🔥 2. Accessing Values
print(tp[0])
print(tp[-1])

#🔥 3. Tuple is Immutable (cannot modify)
tp = (10, 20, 30)
# tp[1] = 50   # ❌ ERROR

#🔥 4. Tuple → List → Tuple (अगर बदलना हो)
tp = (10, 20, 30)
lst = list(tp)
lst[1] = 50
tp = tuple(lst)
print(tp)
 
#  🔥 5. Tuple Packing & Unpacking
student = ("Shashi", 21, "Delhi")
name, age, city = student
print(name, age, city)


# 🔥 6. Special Case — Single Element Tuple
tp = (5,)    # comma जरूरी है

