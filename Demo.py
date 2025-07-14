#first_name=input("Enter your first name:")
#last_name=input("Enter your last name:")
#print("Hello " + first_name + " " + last_name)
from cmath import log10
from time import process_time_ns

#first_name="Subhadip"
#last_name='Biswas'
#print(first_name)
#print(last_name)
#print (first_name + " " + last_name)

#data="I don't know any programming language"
#print(data)

#data= "\"Are you okay?\""
#print(data)

#sent="I love Python"
#print(len(sent))
#print(sent.index('P'))
#print(sent.lower())
#print(sent.upper())
#print(sent.islower())
#print(sent.count('o'))
#sent="I LOVE PYTHON"
#print(sent.isupper())


#myLan="I know {}".format("Python")
#print(myLan)

#name="Subhadip"
#prog='Python'
#print(f"My name is {name} and I know {prog}")

#sent="PythonIsVeryEasy"
#print(sent[5])
#print(sent[-6])
#print(sent[2:6])
#print(sent[::3])
#print(sent[::-1])

#sent="MyNameIsSubhadipBiswas"
#print(sent[2:6])

#list1=[10,30,60,90]
#print(list1)
#print(len(list1))

#list2=["Subhadip",30,60,90, True]
#print(list2)
#print(len(list2))

#list3=list1+list2
#print(list3)
#print(len(list3))
#print(list2[-2])

#list4=["Subhadip",30,60,90,90,90,90, "Python"]
#print(list4.count(90))
#print(list4[0:2])
#list4[0]=10
#print(list4)
#list4.append(100)
#print(list4)
#list4.insert(0,999)
#print(list4)

#list1=[10,20,30,40,50]
#list2=["Python","Java"]
#list3="I love"
#list1.extend(list2)
#print(list1)
#list2.extend(list3)
#print(list2)
#list2.pop(3)
#print(list2)

#list1=[20,40,30,10,50]
#print(list1)
#list1.sort()
#print(list1)
#list1.reverse()
#print(list1)

#mylist=[10,20,30,["Python", "Java", "Selenium"]]
#print(mylist)
#print(mylist[3][1])

#emp={"QA":"Subhadip","Dev":"Akash","DevOps":"Rahul","BA":1234,1122:"Manager"}
#print(emp)
#print(type(emp))
#print(emp["Dev"])


#emp={"QA":["Subhadip","Subham","Aarav"],"Dev":"Akash","DevOps":"Rahul","BA":1234,1122:"Manager"}
#print(emp["QA"][1])


#emp={"QA":"Subhadip","Dev":{"FE":"Akash","BE":"Rahul"}}
#print(emp.get("Dev").get("FE"))
#print(emp["Dev"]["BE"])

#emp["Manager"]="XYZ"
#print(emp)

#emp["Manager"]="Samir"
#print(emp)

#emp.pop("QA")
#print(emp)

#emp.popitem()
#print(emp)

#print(len(emp))
#print(emp.keys())
#print(emp.values())
#print(emp.items())


#emp=dict(QA="Subhadip",Dev="Akash",qa="Rahul",Qa="Tamal", DevOps="Akash")
#print(emp)

#enwemp=dict([(1,"Python"),(2,"Java"),(3,"JS")])
#print(enwemp)


#tup1=(1,"Python",98.25, True,1,1,1,"QA",2,2,2)
#print(type(tup1))
#print(tup1)

#l1=list(tup1)
#print(type(l1))
#print(l1)

#s1=set(tup1)
#print(type(s1))
#print(s1)

#tup1=("Subhadip","Subham")
#print(tup1)
#print(len(tup1))

#l1=[(1,3,5),(2,4,6),(11,22,33)]
#print(l1[2][2])


#t1=tuple(["Subhadip","QA","Python"])
#x,y,z=t1
#print(x)



# print("Python Code")
#
# a=20
# if a>40:
#     print("Hello")
#
# else:
#     print("Bye")
#
# print("Python Code End")

# print("Python Code")
#
# name="Python"
# if name=="Python":
#     print("Python found")
# else:
#     print("Python not found")
#
# print("Python Code End")


# print("Python Code")
# lang=input("Enter your language: ")
# #lang="Python"
# if lang=="Java":
#     print("Java found")
# elif lang=="C++":
#     print("C++ found")
# elif lang=="Python":
#     print("Python found")
# else:
#     print("Sorry, Nothing found")
#
# print("Python Code End")


# salary=input("Enter your salary for loan: ")
# sal=int(salary)
# if sal>25000:
#     print("You are eligible for car loan")
#     if sal>50000:
#         print("You are eligible for home loan")
#         if sal>75000:
#             print("You are eligible for personal loan")
# else:
#     print("You are not eligible for loan")

# status=False
# names=["Python","Java","Selenium","JS"]
#
# for name in names:
#     if name == "Java":
#         status=True
#         break
#     else:
#         print("Please wait we are still searching...")
#
# if status:
#     print("We found the record")
# else:
#     print("We did not find the record")


# name="Python"
# for a in name:
#     print(a)


# finalMarks=0
# for m in [25,50,75,100]:
#     finalMarks=finalMarks+m
#     #print(finalMarks)
#
# result=str(finalMarks)
# print("Final marks is "+result)


# sent={10,20,30,"Python",90.99,"Java"}
# for abc in sent:
#     print(abc)

# mydict={1:"Python",2:"Java","Lang":"JS"}
# for d in mydict:
#     print(d)

# for d in mydict.items():
#     print(d)


# for a,b in mydict.items():
#     print(a)
#     print(b)

# for a in mydict.values():
#     print(a)


# evenList=[]
# oddList=[]
#
# for x in range(50):
#     if x % 2 == 0:
#         evenList.append(x)
#     else:
#         oddList.append(x)
#
# print(evenList)
# print(oddList)

# l1=["Subhadip","Subham","Aarav"]
# l2=["Python","Java","JS"]
# l3=["India","US","UK"]
#
# for x in l1:
#     for y in l2:
#         for z in l3:
#             print(x + " "+y+" "+z)



# t1=(1,3,5)
# t2=(2,4,6)
# t3=(10,20,30)
#
# l1=[t1,t2,t3]
# print(l1)

# for x in l1:
#     print(x)

# for x,y,z in l1:
#     print(x)
#     print(y)
#     print(z)


# x=1
# while x<10:
#     print(x)
#     x=x+1


# num=10
#
# while num<15:
#     print(num)
#     num=num+1
# else:
#     print("Above condition is no more true")

# num=15
#
# while num<30:
#     print(num)
#     num=num+1
#     if num==20:
#         print(num)
#         break
# else:
#     print("Condition is not more true")

# num=1
# while num<10:
#     num=num+1
#     if num==5:
#         continue
#     print(num)
# else:
#     print("Condition is not more true")



# feedback=""
#
# while feedback not in ["10", "9", "8", "7", "6"]:
#     feedback=input("Please enter your feedback...")
#     print("Thank you!")

# def helloworld():
#     print("Hello Python!")
#     c=10+20
#     print(c)
#     print("Bye")
#
#
# def sum(num1,num2):
#     result=num1+num2
#     print("The result is",result)
#
# helloworld()
# sum(10,30)


# def sum(num1,num2,num3=0):
#     result=num1+num2+num3
#     #print("The result is",result)
#     return result
#
# newResult=sum(10,20)
# print("The result is",newResult)

# def greeting(fname,lname,marks):
#     print("Hello " + fname + " " + lname +" "+ str(marks))
#
# greeting("Subhadip","Biswas", marks=95)
# greeting(marks=69, lname="Biswas",fname="Subhadip")

# def check_even_number(num):
#     result= num % 2 == 0
#     print(result)
#
# check_even_number(5)


# def check_even_number(list1):
#     even_number=[]
#     for i in list1:
#         if i%2==0:
#             even_number.append(i)
#         else:
#           pass
#     return even_number
#
# result=check_even_number([1,2,3,4,5,6,7,8,9,10])
# print(result)


# def check_odd_number(list1):
#     odd_number = []
#     for i in list1:
#         if i % 2 == 0:
#           pass
#         else:
#           odd_number.append(i)
#     return odd_number
#
# result = check_odd_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(result)


# def check_odd_number(list1):
#     odd_number = []
#     for i in list1:
#         if i % 2 == 0:
#           pass
#         else:
#          odd_number.append(i)
#     return odd_number
#
#
# result = check_odd_number([2, 4, 6, 8, 10])
#
# if len(result)>0:
#     print(result)
# else:
#     print("Sorry no odd number found")


# def print_name(*args):
#  print(args)
#  print(args[1])
#
# print_name("Python","Java","JS","Ruby","C")


# def get_sum_of_all_numbers(*args):
#  print(sum(args))
#
# def get_min_number(*args):
#  print(min(args))
#
# def get_max_number(*args):
#   print(max(args))
#
# get_sum_of_all_numbers(10,20,30)
# get_min_number(1,3,5,7,9)
# get_max_number(2,4,6,8,10)


# def print_name(**kwargs):
#     print(kwargs)
#     print(kwargs['phone'])
#
# print_name(name="Subhadip",address="Kolkata",phone=9830440111)



# def mix_agr(*args,**kwargs):
#  print(args)
#  print(kwargs)
#
# mix_agr(10,20,30,name="Subhadip",country="India")

# import calendar
# import os
# import math
#
# result=calendar.month(2025,6)
# print(os.getcwd())
# print(result)
# print(math.sqrt(4))


# import MyModule
#
# MyModule.Hello_World()
# MyModule.calEMI()
#
# def homeEMI():
#     print("Home EMI is 50K INR")
#
# homeEMI()

# from MyModule import Hello_World
# from MyModule import calEMI
# from MyModule import *
#
# Hello_World()
# calEMI()


# from MyPackage.MyModule import *
# hello_world()
# cal_emi()

# data=lambda num:num*num
# result=data(2)
# print(result)
#
# newData=lambda num1,num2,num3:num1*num2+num2*3+num3*4
# print(newData(1,2,3))

