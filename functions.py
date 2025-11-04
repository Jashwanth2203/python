# def addition():
#     num1=int(input('enter a number:'))
#     num2=int(input('enter the number:'))
#     print(num1+num2)
# addition()

# greatest of three numbers:

# def greatest(a,b,c):
#     if a>b and a>c:
#         print ('a is greatest')
#     elif b>c and b>a:
#         print ('b is greatest')
#     else:
#         print ('c is greatest')
#     return(a,b,c)   
# greatest(3,4,2)

# multiple return statement:

# def add2(a,b):
#     return a+b,a-b,a*b,a/b,a%b
# print(add2(2,3))

# def greet(name,position,company):
#     print(f'''Welcome {name}, You are our new {position}, Hope you take {company} to new heights''')
# greet('Jashwanth','CEO','Apple')

# def product(a=1,b=1,c=1):
#     return a*b*c
# print(product(1,2,3))
# print(product())

#write a program to calculate total bill of a costomer at a restaurant.
# parameters: no of items,quantity,tax,discount

# def bill(items,quantity,prices,tax,discount,delivery):
#     list1=['chicken biryani','crispy chicken','roti','sweet']
#     bill=0
#     for i in list1:
#         print('no of quantity:',i)
#         item1=int(input('quantity:'))
#         sum=sum+item1*prices[i]

# list1=['chicken biryani','crispy chicken','roti','sweet']
# bill=0
# for i in range(len(list1)):
#     print('no of quantity:',i)

# def rectangle(l=2,b=1):
#     area=l*b
#     print("area :",area)
#     perimeter=2*(l+b)
#     print('perimeter=',perimeter)
# rectangle(6,4)

# def product(*numbers):
#     product=1
#     for num in numbers:
#         product*=num
#     return product
# print('Product:',product(1,2,3,4,5,6))

# def Batch(**details):
#     for i in details.values():
#         print(i)
# Batch(name='viswa',age=25,place='kodad')

# def result(**details):
#     sum=0
#     for i in details:
#         sum+=details[i]
#     print('Total marks:',sum)
#     subjects=print(len(details))
#     percentage=(sum/(len(details)*100))*100
#     print('percentage=',percentage)
# result(maths=96,physics=86,chemistry=90)

# def combine(*words):
#    sentance=''
#    for i in range((words)):
#        sentance+=i
#     print('sentance=',sentance)
# combine('Welcome ','jashwanth ',', ','You ', 'are ','our ','new ','CEO.',' Hope',' you',' take',' Apple',' to',' new',' heights')

#arthimetic operations

# def add(a,b):
#     print('addition=',a+b)
#     print('subtraction=',a-b)
#     print('multiplication=',a*b)
#     print('dividion='a/b)
# print(add(2,3))

# #factorial

# def fact(a,b):
#     sum=1
#     for i in range(a,b+1):
#         sum*=i
#     print('factorial=',sum)
# fact(1,5)

# # fibonacci

# def fib(n):
#     a,b=0,1
#     for i in range(n):
#         print(a)
#         a,b=b,a+b
# fib(10)

# perfect number

# def perfect(n):
#     sum=0
#     list1=[]
#     for i in range(1,n):
#         if n%i==0:
#             list1+=[i]
#             sum+=i
#     print('sum=',sum)
#     print('numbers=',list1)
#     if n==sum:
#         print('perfect number')
#     else:
#         print('not perfect number')
# perfect(int(input('enter the number:')))

# def prime(n):
#     for i in range(2,n+1):
#         if n%i!=0:
#             print('prime number')
#             break
#         else:
#             print('not a prime number')
#             break
# prime(int(input('enter the number:')))

def prime(n):
    list1=[]
    for j in range(1,n+1):
        for i in range(2,(j**0.5)+1):
            if n%i!=0:
                list1+=[i]
    print('prime numbers=',list1)
prime(int(input('enter the number:')))