#1 Find the sum of all elements in a list
l = [1,2,3,4,5]
print(sum(l))

#2 Find the largest element in a list
l = [2,1,3,4,21]
print(max(l))

#3 Find the smallest element in a list
l = [221,923,45,65,78]
print(min(l))

#4 Count even and odd numbers in a list
l = [12,23,45,567,89]
countOdd = 0
countEven = 0
for val in l:
    if val%2 == 0:
        countEven += 1
    else:
        countOdd += 1
print("Even -> ", countEven)
print("Odd -> ", countOdd)

# Remove duplicate elements from a list
l = [12,12,23,34,34,45,56]
s = set(l)
l = list(s)
print(l)

 
# Sort a list in ascending order
l = [12,23,45,67,89,43,21]
l.sort()
print("Asc -> ",l)

# Sort a list in descending order
lst = [1,23,45,32,12]
lst.sort(reverse=True)
print("Des -> ", lst)

# Find the second largest element
lst = [1,42,40,3,5,12]
first,second = -1,-1
for val in lst:
    if val > first:
        second = first   
        first = val
    elif val > second:
        second = val   

print(first, second)

# Reverse a list
l = [1,2,3,4,5]
# print("1st method", l[::-1])
n = len(l)  #5
for i in range(n//2):
    temp = l[i]
    l[i] = l[n-i-1]
    l[n-i-1] = temp
print("Reversed List-> ", l)

# Merge two lists
l1 = [1,2,3]
l2 = [12,3,45]

print(l1+l2)