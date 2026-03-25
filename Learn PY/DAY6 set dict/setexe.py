# 1️⃣ Basics

# Set kya hota hai? List se kaise different hai?

# Set me duplicate values ka kya hota hai?

# Set unordered hota hai ya ordered?

# Ek list se duplicates remove karo using set

# Check karo ek element set me hai ya nahi
s = {1,2,3,4}
if 2 in s:
    print("yes")


# Do sets ka union, intersection, difference nikalo
A = {1,2,3}
B = {3,4,5}
print(A | B) # union
print(A & B) # intersection
print(A - B) # difference


# Common elements find karo from two lists
l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]
s1 = set(l1)
s2 = set(l2)

print(set(l1) & set(l2))

# Set se duplicate remove karke list banao
s1 = {1,2,3,3,4,5}
lst = list(s1)
print(lst)

# Set ke sabse bade aur chhote elements find karo
s1 = {1,2,3,4,5,6}
print(min(s1))
print(max(s1))

# Do sets equal hain ya nahi check karo
s1 = {1,2,3}
s2 = {1,2,3}
print(s1 == s2)


# Frozenset kya hota hai? 
''' Set ke jaisa hi hota hai but immutable ek bar banne ke bad
na ele add kar sakte hai na remove

.IMMUTABLE  .UNORDERED  .UNIQUE ELEMENTS  .
SYNTAX -> frozenset()
ex -> fs = frozenset([1,2,3,2])  -> OP:- frozenset({1,2,3})
'''

#Kab use karte hain?
''' 1. Dictonary ki key banane me
    2. set ke ander set dalne me "set of sets"
    3. Data integrity ke liye (read-only collection)
        '''
# Set indexing kyu nahi hoti?
'''beacause set unordered hota hai'''

# Set mutable hai ya immutable?
''' mutable but frozenset immutable '''