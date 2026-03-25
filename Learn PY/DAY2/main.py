# Input in Python
name = input("Enter your name: ")
print("Hello", name)

# Output in Python
print("Hello Python")
print("Sum =", 10 + 5)

# Type Casting (Conversion)
# input() हमेशा string देता है
# अगर आपको number चाहिए → convert करना पड़ेगा

# String → Integer
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("Sum =", a + b)

# String → Float
x = float(input("Enter price: "))
print(x)


#Operators in Python
#Arithmetic Operators
a = 10
b = 3

print(a + b)   # addition
print(a - b)   # subtraction
print(a * b)   # multiplication
print(a / b)   # division
print(a // b)  # floor division
print(a % b)   # modulus (remainder)
print(a ** b)  # power (10^3)


# Comparison Operators
# (True/False return करते हैं)
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 5)
print(10 >= 5)
print(10 <= 5)

# Logical Operators
age = 20

print(age > 18 and age < 30)
print(age > 18 or age > 30)
print(not(age > 18))

# Assignment Operators
x = 10
x += 5   # x = x + 5
x -= 3   # x = x - 3
