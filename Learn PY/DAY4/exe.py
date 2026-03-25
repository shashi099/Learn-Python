# 🎯 DAY 4 – Exercises (Solve these)

# 1️⃣ Write a function to add 3 numbers
def add(*a):
    print(sum(a))
add(1,2,3)

def Add(a,b,c):
    print(a+b+c)
Add(23,1,1)

# 2️⃣ Function to check age > 18 or not
def checkAge(age):
    if age > 18:
        return "yes"
    return "NO"

print(checkAge(2))

# 3️⃣ Function to return square & cube of a number
def squareCube(num):
    square = num*num
    cube = num*num*num
    return square,cube

print(squareCube(3))

# 4️⃣ Function that counts vowels in a string
def countVowels(alphabets):
    totalCount = 0
    for char in alphabets:
        if char == 'a' or char == 'A':
            totalCount +=1
        if char == 'e' or char == 'E':
            totalCount +=1
        if char == 'i' or char == 'I':
            totalCount +=1
        if char == 'o' or char == 'O':
            totalCount +=1
        if char == 'u' or char == 'U':
            totalCount +=1
    return totalCount

print(countVowels("SHASHIaeiou"))

#2nd way

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

# Example
s = "Hello World"
print(count_vowels(s))   # Output: 3


#3rd way
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    text = text.lower()
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("HELLO"))
# Output: 2

#4th way
def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

print(count_vowels("Beautiful")) 
# Output: 5

# 5️⃣ Function using *args to find maximum number

def findMax(*args):
    print(max(args))

findMax(1,2,21,3)

#2nd way
def Max(*args):
    if not args:
        return None

    maximum = args[0]
    for i in args:
        if maximum <= i:
           maximum = i
    return maximum
print(Max(1,2,3,4,21,32,21))
