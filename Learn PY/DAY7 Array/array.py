#In Python, arrays are usually implemented using list.

'''🔹 Creating Arrays'''
arr = []        #empty array
arr = [1,2,3,4]
arr = list((4,5,6))


'''🔹 Accessing Elements (Indexing)'''

arr = [10,20,30]

print(arr[0])   #10
print(arr[-1])  #30  last element

'''🔹 Updating Elements'''
arr[1] = 99
print(arr)   #10,99,20,30

'''🔹 Length of Array'''
print(len(arr))


'''🟡 LEVEL 2: Traversing an Array'''
#Using for loop
for val in arr:
    print(val)

# using index
for i in range(len(arr)):
    print(arr[i])


'''🟡 LEVEL 3: Insertion & Deletion'''
# ➕ Add Elements
arr.append(50)    #add at end
arr.insert(2,65)  #at given index insert

# ➖ Remove Elements
arr.pop(1)     #remove from given index
arr.remove(30) #remove the value from array
arr.pop()      # reomve the last index value



'''🟠 LEVEL 4: Important Array Operations'''

arr = [1,2,3,4]
# Reverse Array
arr.reverse()

# Sort array
arr.sort()              #sort in Ascending order
arr.sort(reverse=True)  #sort in Descending Order

# SUM/ MIN/ MAX
print(sum(arr))
print(max(arr))
print(min(arr))


'''🟠 LEVEL 5: Searching in Array'''
# Linear Search
arr = [1,2,3,4,5]
target = 3

for i in arr:
    if i == target:
        print("Found")

# Using Python       
if target in arr:
    print("Found")


'''🔵 LEVEL 6: Array Slicing (Very Important)'''

arr = [10,20,30,40,50,60,70]

print(arr[:3])    #[10,20,30]
print(arr[1:4])   #[20,30,40]
print(arr[::2])   #[10,30,50,70]

print(arr[-3:-1]) #[50,60]
print(arr[-4:])   #[40, 50, 60, 70]


'''🔵 LEVEL 7: Common Interview Problems (Beginner-Medium)'''
# 1️⃣ Find Largest Element
arr = [2,5,7,1]
print(max(arr))

# 2️⃣ Second Largest Element
arr = [2,5,6,3,9]
arr.sort()
print(arr[-2])

# 3️⃣ Reverse Array (Without Built-in)
arr = [3,1,7,5]
l, r = 0, len(arr)-1

while(l < r):
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

print(arr)


'''🟣 LEVEL 8: Two Pointer Technique (Intermediate)'''
# Used in many interview questions.

# Example: Check if array is palindrome
arr = [1, 2, 3, 2, 1]
l,r = 0,len(arr)-1
check = True

while(l<=r):
    if arr[l] != arr[r]:
        check = False
        break
    l+=1
    r-=1

print(check)


'''🟣 LEVEL 9: Sliding Window (Intermediate)'''
# Example: Maximum sum of subarray of size k
arr = [2,3,1,2,4,5,2,3]
k = 3

window_sum = sum(arr[:k])
# print(window_sum)
max_sum = window_sum

for i in range(k,len(arr)+1):
    window_sum = sum(arr[i-k:i])
    # print("w = ", window_sum)
    max_sum = max(max_sum, window_sum)
    # print("m ", max_sum)

print(max_sum)


'''🔴 LEVEL 10: Advanced Patterns'''
# Prefix Sum
arr = [1,2,5,2,3]          # ans = [1,3,8,10,13]
 
for i in range(1,len(arr)):
    arr[i] = arr[i] + arr[i-1]

print(arr)