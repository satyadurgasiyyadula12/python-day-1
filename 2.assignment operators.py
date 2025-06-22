
"""
AN OPEARATOR IS a special symbol which is used to perform an operator
eg:c=a+b
herec,a,b are operands
+ is a special symbol
The python operators are:
1.Arithmetic operator
2.relational operator
3.logical operator
4.Bitwise operator
5.Identity operator
6.Membership operator
7.Assignment operator
"""


"""
An Arithmetic operator is used to perform some mathematical/arithmatic operations
the operator are +, -, *, /, //,%,**
Note;input()is afunction which takes input fron user
"""

a=int(input("enter a number:"))
b=int(input('enter a number:'))
print("the addition",a+b)
print("the subtraction",a-b)
print("the multiplication",a*b)
nt("The modulardivision ", a%b)#which returns the remainder part before the decimal 
print("The power ",a**b)#which returns the power 
""" 
//#which returns the integral quotient part in a division 
%#which returns the remainder part before the decimal 
""" 
""" 
Relational/Comparison Operators are used to compare the values 
and return the boolean they are 
>, <, >=, <=, ==, != 
""" 
a = int(input("enter a number: ")) 
b = int(input("enter a number: ")) 
print("The greater value ", a>b) 
print("The lesser value ", a<b) 
print("The greater than or equals too value ", a>=b) 
print("The less than or equals too value  ", a<=b) 
print("The equals too value ", a==b) 
print("The not equals too value ", a!=b) 
"""Logical operators are used to perform logical operations 
they are logical and , or , not 
and -- if both the conditions are true it returns the true 
T T T 
F T F 
T F F 
F F F 
or --- if one of the condition is true it returns the true 
T F T 
F T T 
T T T 
F F F 
not -- it just negotiates the condition 
T F 
F T 
""" 
a = 13 
b = 45 
c= a>=34 and b<=50 
print(c) 
d = 67 
e = 89 
f = d!=67 or e==89 
print(f) 
a = 10 
print(not(a))#F 
b = 0 
print(not(b))#T 
""" 
bitwise operators are used to perform binary operations they are: 
bitwise and(&): if both the  bit are "1" it returns 1 
bitwise or (|): if one of the bit is "1" it returns 1 
bitwise xor(^): if one of the bit is "1" it returns "1" 
and if both the bits are "1" it returns "0"   
""" 
a = 5 
b = 9 
c = a&b 
print(c) 
d = 15 
e = 13 
f = d|e 
print(f) 
g = 12 
h = 14 
i =g^h 
print(i) 
""" 
Membership operators are used to check the values in a sequence 
and returns the boolean values 
they operators are "in","not in" 
""" 
x = [ "apple", "banana"] 
print("apple" in x) 
print("pp" not in x) 
print("banana" not in x) 
print("dragon" in x) 
""" 
identity operators are used to compare the values 
and return the boolean values.. 
the operators are "is", "is not" 
""" 
x = [ 1,2,3] 
y = [ 4, 5,6] 
z = x 
print(x is y)#F 
print(x is z)#T 
print(y is z)#F 
print(y is not z)#T 
print(z is not x)#F 
print(x is not y)#T
