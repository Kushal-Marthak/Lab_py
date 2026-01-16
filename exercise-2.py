Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
for i in range(1, 6):
    print(i)

1
2
3
4
5
text = "Python"
length = len(text)
print(length)
SyntaxError: multiple statements found while compiling a single statement
text = "Python"
length = len(text)
print(length)
6
KeyboardInterrupt
a = 10
b = 20
print(max(a, b))
20
print("Welcome")
Welcome
text = "Python"
print(text[0])
P
KeyboardInterrupt
P = float(input("Enter principal amount: "))
Enter principal amount: 1000
R = float(input("Enter rate of interest: "))
Enter rate of interest: 5
T = float(input("Enter time in years: "))
Enter time in years: 2
SI = (P * R * T) / 100
print("Simple Interest =", SI)
Simple Interest = 100.0
text = "Python"
print(text[-1])
n
s = input("Enter a string: ")
Enter a string: 
\

Enter a number: -5
SyntaxError: invalid syntax
KeyboardInterrupt
num = int(input("Enter a number: "))
Enter a number: -5

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

    
Negative number
a, b, c = 10, 20, 30
print(a + b + c)
60
num1 = float(input("Enter first number: "))
Enter first number: 5
num2 = float(input("Enter second number: "))
Enter second number: 10
sum = num1 + num2
print("The sum of the numbers is:", sum)
The sum of the numbers is: 15.0
