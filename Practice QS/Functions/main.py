#1 Create a function to add two numbers
def addTwoNumber(a,b):
    return a+b
print(addTwoNumber(1,2))

# Create a function to check even or odd
def checkEvenOdd(num):
    return "Even" if num%2==0 else "Odd"
print(checkEvenOdd(121))

# Create a function to find factorial
def findFact(num):
    fact = 1
    while(num > 0):
        fact *= num
        num = num-1
    return fact
print(findFact(5))

# Create a function to check prime number
def checkPrime(num):
    if num <= 3:
        return True
    else:
        for i in range(2,num//2+1):
            if num%i==0:
                return False
    return True
print(checkPrime(7))    

# Create a function to count vowels in a string
def countVowel(s):
    vowel = "aeiou"
    count = 0
    for ch in s:
        if ch in vowel:
            count+=1
    return count
print(countVowel("shashi"))

# Create a function using *args to find maximum number
def findMax(*args):
    return max(args)
print(findMax(1,21,3,46,5))
print(findMax(21,34))

# Create a function using **kwargs
# जब arguments key-value pair में हों:
def printDict(**details):
    print(details)
printDict(name="shashi", age=21, college="XYZ")

'''def info(**details):
    print(details)

info(name="Shashi", age=20, city="Delhi")'''

 
# Create a function to return square of a number
def findSquare(num):
    return num*num

square = findSquare(12)
print(square)

# Create a function to reverse a string
def revString(s):
    return s[::-1]

rev = revString("Shashi")
print(rev)

# Create a recursive function to find factorial
def calFact(num):
    if num <= 1:
        return 1
    return num * calFact(num-1)

factorial = calFact(5)
print(factorial)