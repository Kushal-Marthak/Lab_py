Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 1.assignment operator
x = 10
print(x)
10
# 2.urnary minus
a = 5
print(-a)
-5
# 3.relational
P = 10
q = 5
print(p>q)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(p>q)
NameError: name 'p' is not defined. Did you mean: 'P'?
# 3.relational
p = 10
q = 5
print(p>q)
True
print(p==q)
False
# 4.logical
x = true
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x = true
NameError: name 'true' is not defined. Did you mean: 'True'?
x = True
y = False
print (x and y)
False
print (x or y)
True
print (not x)
False
# 5.boolean
is_pass = true
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    is_pass = true
NameError: name 'true' is not defined. Did you mean: 'True'?
is_pass = True
print(is_pass)  #o/p = true
True
# 6.bitwise
a=5
b=3
print(a & b)
1
print(a | b)
7
# 7.membership
numbers = [1,2,3,4,6]
print(2 in numbers)
True
print(5 not in numbers)
True
# 8. identity
x = 10
y = 10
print(x is y)
True
print( x is not y)
False
