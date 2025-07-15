"""
 a if within a if it is called nested if
 Note:in order to execute inner else outer if condition must be true
 syntax:
 if condition:
    outer if statements
    if codition:
    inner if statements
    else:
    inner else statements
else:
    outer else statements
"""  

     
a=12
b=20
c=30
if a==12 and c==30:
    print("the outer if executed..")
    if a==12:
        print("the inner if executed..")
    else:
        print("the inner else executed..")
else:
    print("the outer else executed..")



# a program on whether advice

is_snowing=True
temp=int(input("enter the temperature.."))
if is_snowing<10:
    print("please carry umbrella..")
    if is_snowing==-10:
        print("please carry umbrella and jacket")
    else:
        print("Enjoy the sunny day!!")
else:
    print("U have a great day")

#Express Delivery
weight=int(input("enter the weight.."))
if weight<=4:
    print("the delivery can be expected within 24 hrs..")
    if weight>10:
        print("need to pay an extra amount for extra weight..")
    else:
        print("no need to pay any extra charge have a great delivery!!")
else:
    print("need to wait 3-5 business days to expert the delivery")

"""
shorthand if:writing a if in a line is called shoorthand if
syntax:if condition: statements
"""
a=10
if a==15:
    print(True)



"""
#looping statements
looping statements are also called as iterative statements
these statements are used to run a particular condition
no of times...
they are divided into "2" types
1.while
2.for

(while(true execute) or entry control loop)
"""
"""
while;while condition:
            statements
            exit condition/incrementation
"""

#eg:
i=1
while i<=10:
    #print(i)-->in this particular line the
    #"i"value runs"n"times because no incrementation/exit cond specify
     print("the value",i)
     i+=1


#eg2:
#while True:
    #print("the while condition")
#note: as default condition is true the while loop runs"infinity"times

#eg3:
#while False:
    #print("the while condition")
#as while is also called entry control
# loop it just checks the conditionin the entrance
# as default False is given as condition it wont execute


"""
Jumping/Transfer statements:
These statements are used to control the normal
execution of a program they are of"2" types
1.Break : this statement is used toterminate/break the loop
2. Continue:this statement are used to skip current iteration and run the next iteration
"""
i+=0
while i<=10:
    i+=1
    if i==6:
         break#terminates/stops the program
    print(i)

i=0
while i<=9:
    i+=1
    if i==3:
        continue#skip the current iteration
    print(i)
    
