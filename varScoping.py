# local variable

# def add():
#     a=10
#     b=20
#     print(a+b)
# # print(a) it is a error due to defined not outside the function
# add()

# def details():
#     name='jashwanth'
#     age=22
#     place='hyderabad'
#     print(name,age,place)
# details()
# # print(name)

# Non-local variable

# def institute():
#     name='10k coders'
#     def batch():
#         name='75R'
#         print(name)
#     batch()
#     print(name)
# institute()

# def addition(a,b):
#     n=a+b
#     def multiplication():
#         n=a*b
#         m=a-b
#         print('multiplication=',n)
#     print('addition=',n)
#     # print(m) #this gives error
#     multiplication()
# addition(2,3)

# global variable

# glbvar='this is global variable'

# def func1():
#     print('this is function 1')
#     print(glbvar)

# def func2():
#     print('this is function2')
#     def func3():
#         print(glbvar)
#     func3()
# func1()
# func2()

# a=20

# def glodemo():
#     global a
#     a=15
#     print(a)
# print(a)
# glodemo()

# name='jashwanth'
# def details():
#     name='viswa'
#     def func1():
#         global name
#         name='swaroop'
#         print(name)
#     func1()
#     print(name)
# details()
# print(name)

# non global variable

# name='jashwanth'
# def details():
#     name='viswa'
#     def func1():
#         nonlocal name
#         name='swaroop'
#         print(name)
#     func1()
#     print(name)
# details()
# print(name)

# len='jashwanth'
# print(len)

