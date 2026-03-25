'''
⭐ PART 1 — LISTS

List = Python का most used data structure
👉 Ordered
👉 Changeable (mutable)
👉 Duplicate values allowed
👉 Elements → [] square brackets में
'''

#🔥 1. Create List
numbers = [10, 20, 30, 40]
names = ["shashi", "rahul", "amit"]
mixed = [10, "hello", 3.14, True]


#🔥 2. Accessing Elements (Indexing)
fruits = ["apple", "banana", "mango"]

print(fruits[0])   # apple
print(fruits[-1])  # mango

#🔥 3. Changing List Values
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)


#🔥 4. Adding Elements
#append() → end में जोड़ता है
fruits.append("grapes")

#insert() → किसी index पर insert
fruits.insert(1, "kiwi")

# 🔥 5. Removing Elements
fruits.remove("banana")
fruits.pop()     # last element remove
fruits.pop(1)    # index remove
del fruits[0]    # delete by index

#🔥 7. Lists in Loops
for item in fruits:
    print(item)

#🔥 6. List Slicing
nums = [1, 2, 3, 4, 5]
print(nums[1:4])   # 2,3,4
print(nums[:3])    # 1,2,3
print(nums[2:])    # 3,4,5

# 🔥 8. check if element exists
if "apple" in fruits:
    print("Found")

# 🔥 9. List Comprehension (Very Important)
# Short method to create lists:

nums = [x*x for x in range(1, 6)]
print(nums)      # [1,4,9,16,25]
