# 1 Print "Hello Python"

#2 Take user input and print it

#3 Add two numbers entered by the user
'''a = int(input("Enter 1st numbers"))
b = int(input("Enter 2nd numbers"))
print(a+b)'''

#4 Check whether a number is even or odd
'''num = int(input())
print("EVEN") if num%2==0 else print("ODD")'''

#5 Check whether a number is positive, negative, or zero
'''num = int(input())
if num > 0:
    print("+ve")
elif num < 0:
    print("-ve")
else:
    print("0")'''

#6 Find the largest of two numbers
'''print(max(12,1))
'''
#7 Find the largest of three numbers
'''print(max(1,2,3))
'''
#8 Swap two variables
'''a = 12
b = 21
temp = a+b
a = temp-a
b = temp-a
print("a= ",a)
print("b= ",b)'''

#9 Convert Celsius to Fahrenheit
'''cel = int(input("Give the Input of Cel"))
Faren = float(1.8*cel + 32)
print(Faren)'''


#10 Find the square and cube of a number
n = int(input("Enter a number"))
square = (n*n)
print("Square -> ",square)
cube = (n*n*n)
print("Cube -> ", cube)
