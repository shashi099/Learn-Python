# 1️⃣ Create a tuple of 4 elements and print them
t = (11,21,3,14)
print(t)

# 2️⃣ Find maximum value in tuple
max = t[0]
for num in t:
    if num >= max:
        max = num
print(max)    
# print(max(1,2,3,4,11))
# 3️⃣ Convert tuple to list
lst = list(t)
print(lst)

# 4️⃣ Check if an element exists in tuple
def isExist(tp,ele):
    for i in tp:
        return True if i == ele else False
ans = isExist((10,20,30,40,50),10)
print(ans)

# 5️⃣ Print tuple in reverse order
tpl = (10,20,30,40,50)
print(tpl[::-1])

#2
rev = tuple(reversed(tpl))
print(rev)

#3
t = (10, 20, 30, 40)
rev = ()

for i in range(len(t)-1, -1, -1):
    rev += (t[i],)

print(rev)


