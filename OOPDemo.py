# class Person:
#     def welcome(self):
#        print("Welcome To Python")
#
#     def hello_world(self):
#         print("Hello World")
#
#     def sum(self,num1,num2):
#         print (num1+num2)
#
# # p=Person()
# # #Person.welcome(p)
# # p.welcome()
# # p.sum(10,20)
#
# p=Person()
# p.name="Subhadip"
# p.phone=9830440111
# p.country="India"
#
# q=Person()
# q.name="Subham"
# q.phone=9830330111
# q.country="USA"
#
# print(p.name)
# print(q.phone)

# class Person:
#     def __init__(self,f,l):
#         self.fname=f
#         self.lname=l
#         print("Hello "+self.fname+" "+self.lname)
#
#     def sum(self,x,y):
#         self.v1=x
#         self.v2=y
#         return self.v1+self.v2
#
# x=Person("Subhadip","Biswas")
# print(x.sum(10,20))

# class Base:
#     name="Subhadip"
#     def baseMethod(self):
#         print("I am in BaseClass")
#
# class Child(Base):
#     company="INT"
#     def childMethod(self):
#         print("I am in ChildClass")
#
# c=Child()
# c.childMethod()
# c.baseMethod()
# print(c.name)
# print(c.company)

# class classA:
#     def methodA(self):
#         print("I am coming from Class A")
#
#     def hello_world(self):
#         print("hello from class A")
#
#
# class classB(classA):
#     def methodB(self):
#         print("I am coming from Class B")
#
#     def hello_world(self):
#         print("hello from class B")
#
# class classC(classB):
#     def methodC(self):
#         print("I am coming from Class C")
#
#     def hello_world(self):
#         print("hello from class C")
#
# obj1=classC()
# obj1.methodA()
# obj1.methodB()
# obj1.methodC()
# obj1.hello_world()



# class classA:
#     def methodA(self):
#         print("I am coming from Class A")
#
#     def hello_world(self):
#         print("hello from class A")
#
#
# class classB:
#     def methodB(self):
#         print("I am coming from Class B")
#
#     def hello_world(self):
#         print("hello from class B")
#
# class classC(classA,classB):
#     def methodC(self):
#         print("I am coming from Class C")
#
#     def hello_world(self):
#         print("hello from class C")
#
# c=classC()
# # c.methodA()
# # c.methodB()
# # c.methodC()
# c.hello_world()
# print(classC.mro())



# class A:
#     def sum(self):
#         print("Calling from A - Sum of two numbers is 10")
#
# class B(A):
#     def sum(self):
#         print("Calling from B - Sum of two numbers is 20")
#
# class C(B):
#     def sum(self):
#         print("Calling from C - Sum of two numbers is 30")
#
# # obj1=A()
# # obj1.sum()
# #
# # obj2=B()
# # obj2.sum()
#
# obj1=C()
# obj1.sum()



# class Greeter:
#     def __init__(self, name):
#         self.name = name
#
#     def hello_world(self):
#         print(f"Hello, {self.name}!")
#
# g = Greeter("Subhadip")
# g.hello_world()


# class BaseClass:
#     def hello_world(self):
#         print("Hello Python from base")
#
# class ChildClass(BaseClass):
#     def hello_world(self):
#         super().hello_world()
#         #BaseClass.hello_world(self)
#         print("Hello Python from child")
#
# obj1=ChildClass()
# obj1.hello_world()



# class A:
#     def __init__(self):
#         print("I am in class A")
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         #A.__init__(self)
#         print("I am in class B")
#
# class C(B):
#     def __init__(self):
#         #A.__init__(self)
#         #B.__init__(self)
#         super().__init__()
#         print("I am in class C")
#
# obj1=C()


#SyntaxError-------------------
#while True print("Hello World")


try:
    content=open("D:\\PyCharmWorkplace\\Python\\Demo1.txt","r")
    print(content.read())
    print("Have a nice day!")
except FileNotFoundError as err:
    print("Something went wrong", err)

print("This is last statement")

# try:
#     num1=int(input("Please enter first number:"))
#     num2=int(input("Please enter second number:"))
#     result=num1/num2
#     print("Result is ",result)
# except TypeError as err:
#     print("Please provide only digits", err)
# except ZeroDivisionError as err:
#     print("Please do not enter zero", err)
# except ValueError as err:
#     print("Please provide valid entry", err)
# except Exception as err:
#     print("Something went wrong", err)
# else:
#     print("All went right")
# finally:
#     print("Have a good day")



# num=int(input("Enter a number"))
# if num>0:
#     raise AssertionError
# print("The number is ",num)



# assert "Selenium" in "Selenium is for Web Automation", "Validation Failed"
# print("Validation 1 Passed")
#
# str1="Python"
# str2="Python"
# assert str1==str2, "String matching Failed"
# print("Validation 2 Passed")
#
# assert "Python" in ["C", "Java", "Python", "JS"], "Python is not present"
# print("Validation 3 Passed")


