#🔥 1. for loop

#range(5) = 0 से 4 तक numbers देता है → Total 5 times loop चलता है।
for i in range(5):
    print(i)

#⭐ RANGE() Explained (very important)
#range(5)  -> 0 1 2 3 4
#range(1, 5)  -> 1 2 3 4
#range(1, 10, 2) -> 1 3 5 7 9

#⭐ Loop over a List
fruits = ["apple", "mango", "banana"]

for item in fruits:
    print(item)

#⭐ Loop over String
for char in "Python":
    print(char)

#⭐ Using break
for i in range(10):
    if i == 5:
        break
    print(i)

#⭐ Using continue
for i in range(10):
    if i == 5:
        continue
    print(i)

# ⭐ Example Task – Sum of first 10 numbers
total = 0
for i in range(1, 11):
    total += i
print(total)





#🔥 2. while loop

#📌 Basic Structure
i = 1

while i <= 5:
    print(i)
    i += 1

#⭐ Infinite Loop (गलती से)
'''while True:
    print("Running...")'''

#⭐ break with while
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

#⭐ continue with while
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)



#⭐ Example: Guess the number game
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess: "))
print("Correct!")


