# DATA TYPES:indicates the type of data that a variable holding on#
"""
data types is a 5 types:
  1.(NUMBER(INT,FLOAT,COMPLEX) 
  2.SEQUENCE(ORDER:list ,tuple ,string)
  3.BOOLEAN(TRUE,FALSE)
  4.SET
  5.dictionary
  """

"""
comments are divided into "2" types
1.single line comments -- are used to represent the line single by #
2. multi line comments --- are used to  sinle quotations and double quotations("")
 comments is like te additional information to understand easily
"""

"""
type() -- which tells about type of a value that internally complier holding on
id()-- which tells about the adress  location of the value
"""
"""
#number#
 NUMBER-- which tells about the number datatypes divided into"3" types
1.integer=int()
2.float=float()
3.complex=a+bj
 """
"""
INTEGER:which holds the all positive and negative whole numbers 0 to n and 0 to -n
represent:int()
"""
a = 123 
print(a)
print(type(a))
print(id(a))

a1=-90 
print(a1)
print(type(a))
print(id(a))

"""
FLOAT -- which holds all the decimal or fractional values i.e., 0 to n ,n and 0 to -n ,n 
it represent float()
"""
b1=-78.67
print(b1)
print(type(b1))
print(id(b1))

"""
COMPLEX DATA TYPES:
 it is used to hold the real and imaginary values 
 it is represented a+bj
"""
c=78+67j
print(c)
print(type(c))
print(id(c))



""" 
#SEQUENCE DATA TYPE#: 
it is order and 
it is divided into"3"types
1.string
2.list
3.tuple
"""

"""
STRING-- it is a group of characters/collection of characters
it is represented as single quote or double quote 
"""
a="satya"
print(a)
print(type(a))
print(id(a))

#print- a value olp type type tell what is what #

"""
LIST-- it is a collection of items (or) values (or) elements
syntax:listname =[val1 ,val2,,,,valn]
"""
satya=[23,24,25,26 ,'hello']  #list/element/value#
print(satya)
print(type(satya))
print(id(satya))

"""
tuple= collection of items
syntax:tuple name
"""
mytuple=((12,23),satya)
print(mytuple)
print(type(mytuple))
print(id(mytuple))
print(mytuple[1])


"""
individual= use indrx()
it is starting 0 to  ending n-1 ,use :( dictionary ,set ,list,tuple)
syntax to access the elements
print(listname[element position])
"""
"""
giving a list within a list is called sublist
gining a tuple within a lis is called subtuple
"""


"""
#BOOLEAN#
This means to check the condition
it is dividedinto "2" types
1.true
 2.false
 it is represent as "bool"
"""

a=True
print(a)
print(type(a))

b=False
print(b)
print(type(b))



#set#
"""
set:it is a collection of values/items/elements,A set not accept list
syntax:setname={val1,vale...valn} it is "flower brackets" 
"""

hi={12,18,14,56+98j, "hello" }
print(hi)
print(type(hi))



"""
#DICTIONARY#
dictionary(key values):it is a collection of key value pairs
syntax: dictionary name={key1:val1,...keyn:valn}
"""

hello= {1:"college","branch":"ece", "district":"east godavari"}
print(hello)
print(type(hello))


