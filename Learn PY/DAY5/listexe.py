# 1️⃣ Create a list of 5 numbers and print their sum
lst = [1,21,3,31,4]
sum=0
for num in lst:
    sum+=num
print(sum)

# 2️⃣ Replace the 3rd element with 100
lst[2] = 100
print(lst)

# 3️⃣ Print only even numbers from a list
list = [10,11,12,13,14,15,16]
for num in list:
    if num % 2 == 0:
        print(num,end=" ")
print()
# single line of code
# [print(num,end=" ") for num in list if num%2 == 0]

# 4️⃣ Reverse a list
ls = [12,13,14,15,16]
inc = 0
while inc <= len(ls)//2:
    temp = ls[inc]
    ls[inc] = ls[len(ls)-inc-1]
    ls[len(ls)-inc-1] = temp
    inc+=1
print(ls)
     
# 2nd
lst = [10, 20, 30, 40]
print(lst[::-1])

# 3rd
lst = [10, 20, 30, 40]
lst.reverse()
print(lst)

# 5th Using Loop
lst = [10, 20, 30, 40]
for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=" ")


# 5️⃣ Count how many times 5 appears
lst = [10,2,5,2,5,5,54]
print()
print(lst.count(5))
