#📘 DAY 4 — Functions (return, arguments, types, scope, examples)

'''
🔥 1. What is a Function?
Function = Code का एक block जो किसी काम को बार-बार use करने लायक बनाता है।
Example:  
'''
def greet():
    print("Hello!")
#Call function:
greet()


'''
🔥 2. Function with Arguments
Arguments = Function को दिए गए input values
'''
def greet(name):
    print("Hello", name)

greet("Shashi")
greet("Rahul")

''' 
🔥 3. Function with Return Value
Return function का output देता है।
'''
def add(a, b):
    return a + b

result = add(5, 10)
print(result)

'''
🔥 4. Default Arguments
अगर कोई value ना दें… default value use होती है।
'''
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Shashi")

'''
🔥 5. Multiple Return Values
'''
def calculate(a, b):
    add = a + b
    sub = a - b
    return add, sub

x, y = calculate(10, 5)
print(x, y)

'''
🔥 6. Keyword Arguments
आप नाम से value दे सकते हैं:
'''
def student(name, age):
    print(name, age)

student(age=20, name="Shashi")


'''
🔥 *7. Variable-Length Arguments (args)
अगर आपको नहीं पता function में कितने arguments आएंगे:
'''
def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)
total(1, 2)

'''
🔥 **8. Dictionary Arguments (kwargs)
जब arguments key-value pair में हों:
'''
def info(**details):
    print(details)

info(name="Shashi", age=20, city="Delhi")


'''
🔥 9. Function Scope (Local vs Global)
Local variable → function के अंदर valid
Global variable → पूरे program में valid
'''
x = 10  # global

def show():
    x = 5  # local
    print(x)

show()
print(x)


'''
🔥 10. Lambda Function (One-line function)
छोटे functions quickly बनाने के लिए:
'''
square = lambda x: x * x
print(square(5))


#⭐ DAY 4 — Mini Examples
#✔ Check even or odd
def check(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(check(11))

#✔ Factorial
def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(fact(5))

