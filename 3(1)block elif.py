"""
when the condition is "if" block failed the elif
block is executes
syntax:
if condition:
     statements
elif condition:
    statements
    statements
"""

#checking the user id and password
userid = input("enter your user id...")
password = input("enter your password...")


if userid=="abc12390" and password=="km@7890":
    print("welcome to our netbanking of kkkkkbank")
elif userid=="jbd2345" and password=="mk@123345":
    print("welcome to our netbanking of nmmbank")
else:
    print("the user id and password is incorrect...try again!!") 

# accept the number of days from the user and calculate the charge  for library according to the following

"""
till 5 numbers:Rs 2/days
6 to 10:Rs 3/day
11 to 15:Rs 4/day
after 15 days:Rs 5/days
""" 

num = int(input("enter the days.."))
if num<=5:
    print("the charge is..",num*2)
elif num>=6 and num<=10:
    print("the charge is..",num*3)
elif num>=11 and num<=15:
    print("the charge is..",num*4)
elif num>15:
    print("the charge is..",num*5)
else:
    print("wrong days selected")

#write a program to accept 2 numbers from user and an operator and perform operation accordingly
"""
num 1:5
num 2:10
opr:+
answer:15           
"""
num1=int(input("enter a number.."))
num2=int(input("enter a number.."))
opr=input("enter a operator:")
if opr=="+":
    print("the answer:",num1+num2)
elif opr=="-":
    print("the answer:",num1-num2)
elif opr=="*":
    print("the answer:",num1*num2)
elif opr=="/":
    print("the answer:",num1/num2)
else:
    print("wrong operator selected..")

#write a program to accept a number from 1 to 12 and display namw ofthe month and days in that month like 1 for january and no.of days31 and so on.


mon_num=int(input("enter the month  number 1 to 12.."))
if mon_num==1:
    print("the month is jan it has 31 days..")
elif mon_num==2:
    print("the month is feb ithas 28 days..")
elif mon_num==3:
    print("the month is march ithas 31 days..")
elif mon_num==4:
    print("the month is april it has 30 days..")
elif mon_num==5:
    print("the month is may it has 31 days..")
elif mon_num==6:
    print("the month is june it has30 days..")
elif mon_num==7:
    print("the month isjuly it has 31 days..")
elif mon_num==8:
    print("the month is aug it has 31 days..")
elif mon_num==9:
    print("the month is sep it has 30 days..")
elif mon_num==10:
    print("the month is oct it has 31 days..")
elif mon_num==11:
    print("the month is nov it has 30 days..")
elif mon_num==12:
    print("the month is dec it has 31 days..")
else:
    print("wrong numbers")

#write a program to display "hello" if a number entered by user is a multiple of 5 otherwise print "bye"

num=int(input("enter a number.."))
if num% 5==0:
    print("hello")
else:
    print("bye")



"""
write a program to display %tage according to following criteria %tage should accept from user
>90-->A
>80 and <=90-->B
>60 and <=80-->C
<=60 ----D
"""

mar1=int(input("enter a marks.."))
if mar1<=60:
    print("D grade..",mar1)
elif mar1>60 and mar1<=80:
    print("C grade..",mar1)
elif mar1>80 and mar1<=90:
    print("B grade..",mar1)
elif mar1>90:
    print("a grade",mar1)
else:
    print("the failed")
