# Convert a tuple to a list
tp = (1,2,3,4)
lst = list(tp)
print(lst)

# Find the maximum element in a tuple
tp = (12,23,45,121)
print(max(tp))

# Find the length of a set
s = {12,23,45,34}
print(len(s))

# Find the union and intersection of two sets
s1, s2 = {1,2,3,4}, {4,3,5,6}
print(s1|s2) #Union
print(s1&s2) #intersection


# Create a dictionary and print all keys and values
dict = {
    "name" : "shashi",
    "age" : 21,
    "college" : "SIRTE",
    1 : "nayan" 
}
print(dict.keys())
print(dict.values())

# Count the frequency of elements in a list using dictionary
lst = [1,2,3,1,3,4]
freq = {}

for val in lst:
    if val in freq:
        freq[val] += 1
    else:
        freq[val] = 1

print(freq)

# Find the key with maximum value in a dictionary
dict = {
    "shashi" : 75,
    "nihal" : 45,
    "shivam" : 35,
    "yash" : 85
}

max_key = max(dict, key=dict.get)
print(max_key)
# print(max(dict.items(), key=lambda x: x[1]))


# Remove a key from dictionary
data = {"a": 1, "b": 2, "c": 3, "d":5, "e":6}
 
del data["b"]
print(data)

data.pop("a")
print(data)

data.popitem()
print(data)
 

# Check whether a key exists in dictionary
data = {1:"a", 2:"b", 3:"c"}
if 1 in data.keys():
    print(True)

# Sort a dictionary by values
dict = {
    "shashi" : 75,
    "nihal" : 45,
    "shivam" : 35,
    "yash" : 85
}
sorted_dict = sorted(dict.items(), key= lambda x:x[1])
print(sorted_dict)
