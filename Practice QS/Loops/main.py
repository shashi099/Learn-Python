#1 Print numbers from 1 to 10
'''
[print(i) for i in range(1,11)]
'''

# Print numbers from 10 to 1
'''
[print(i) for i in range(10, 0, -1)]
'''
# Print all even numbers between 1 and 100
'''
Even = [i for i in range(1,101) if i%2==0]
print(Even)'''

 
# Find the sum of first n natural numbers
#1 By Using List Comprehension
'''
n = int(input("Enter n"))
ans = sum([i for i in range(1,n)]) 
print("SUM = ", ans)'''

#2
'''
sum = 0
for i in range(1,51):
    sum += i
print(sum)    '''


# Print the multiplication table of a number
'''
N = 5
for i in range(1, 11):
    print(N, "x", i, " = ", N*i)'''

# Count the number of digits in a number
'''
n = 1235
count = 0
while(n > 0):
    n = n//10
    count += 1
print(count)
'''
# Reverse a number

n = 123
rev = 0

while(n > 0):
    lastDigit = n % 10
    rev = rev*10 + lastDigit
    n = n // 10

print("reverse Numner -> ", rev)

# Find the factorial of a number
'''
fact = 1
n = 5
while n>0:
    fact*=n
    n=n-1
print(fact)
'''
# Check whether a number is prime
n = 4
import math
is_prime = True
for i in range(2, int(math.sqrt(n))+1):
    if n%i==0:
        is_prime = False
        break
print(is_prime)
 

# Print Fibonacci series up to n terms
'''fn = f(n-1) + f(n-2)
0,1,1,2,3,5,8'''
# using for loop
'''n=8
a,b = 0,1
for i in range(n):
    print(a, end=" ")
    a,b = b,a+b
'''
# using while loop
n = 8
a,b = 0,1
while (n >= 0):
    print(a, end=" ")
    a,b = b,a+b
    n=n-1
