# lambda functions

# # without lambda
# def add(a,b):
#     print(a+b)
# add(1,2)
# # with lambda
# add_num=lambda a,b:a+b
# print(add_num(5,4))

# square_num=lambda a:a*a
# print(square_num(4))

# # to convert celsius to farenhet
# CelToFar=lambda a:(9/5)*a+32
# print(CelToFar(32),'F')

# # write a lambda functions to check even or odd
# evenOdd=lambda num:'Even'if num%2==0 else 'Odd'
# print(evenOdd(7))
# print(evenOdd(4))

# # largest of two numbers
# largest=lambda a,b:'a is largest' if a>b else 'b is largest'
# print(largest(3,5))
# print(largest(9,6))

# students=['viswa','jashwanth','swaroop','samuel','sai kiran']
# students.sort(key=lambda name:len(name))
# print(students)

# # lambda using map()
# list1=[1,2,5,6,4,3]
# sqlist=list(map(lambda num:num**2,list1))
# print(sqlist)

# # lambda with filter
# list2=[1,2,3,4,5,6,7,8,9,10]
# filter_func=list(filter(lambda num:num%2==0, list2))
# print(filter_func)

# reduce function with lambda
from functools import reduce
list1=[1,2,5,6,4,3]
redfun=reduce(lambda num1,num2:num1*num2, list1)
print(redfun)