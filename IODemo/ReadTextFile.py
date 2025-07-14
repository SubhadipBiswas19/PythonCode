# f=open("IOText.txt")
# data=f.read()
# print(f.name)
# print(f.mode)
# print(data)
# print(f.closed)
# f.close()
# #f.read()
# print(f.closed)

# try:
#     f=open("IOText.txt")
#     data=f.read()
# except Exception as err:
#     print("Exception is ",err)
# finally:
#     f.close()


# with open("IOText.txt") as f:
#     print("Current state is ", f.closed)
#     data=f.read()
#     print(data)
#
# print("State of file is ", f.closed)



# import os
#
# with open(os.path.dirname(os.getcwd())+"\\Demo.txt") as f:
#     print("Current state is ", f.closed)
#     data=f.read()
#     print(data)
#
# print("State of file is ", f.closed)



# with open("IOText.txt","w") as f:
#     f.write("New data from Python")



# with open("IOText.txt","a") as f:
#     f.write("\n")
#     f.write("Hello Python")
#     f.write("\t")
#     f.write("from Subhadip")
#     f.write("\n")
#     f.write("Bye")


# name=['Subhadip','Subham','Akash','Mukesh']
# marks=[10,20,30]
# address=['ABC','PQR','XYZ']
# data=zip(name,marks,address)
# #print(data)
# mydata=list(data)
# print(mydata)



# name={'Subhadip','Subham','Akash','Mukesh'}
# marks={10,20,30}
# address={'ABC','PQR','XYZ'}
#
# print(list(zip(name,marks,address)))




name=['Subhadip','Subham','Akash']
marks=[10,20,30]
address=['ABC','PQR','XYZ']

data=zip(name,marks,address)
mydata=list(data)
print(mydata)

a,b,c=zip(*mydata)
print(a)
print(b)
print(c)
