# number functions

# # absolute function
# print(abs(5))
# print(abs(-3))
# print(abs(3+4j))

# #power function
# print(pow(2,2))
# print(pow(2,3,5)) #it returns the value as a**b%c

# # round function
# print(round(2.5))
# print(round(3.5))

# # divmod function
# # divmod(a,b)=(a//b,a%b)
# print(divmod(10,2))
# print(divmod(10,3))

# max() and min()
# list1=[2,3,5,8,4,3]
# tuple1=(2,3,8,4,5,6)
# list1=['viswa','jashwanth','swaroop']
# tuple1=('viswa','jashwanth','swaroop')
# print(max(list1))
# print(min(list1))
# # using list
# maxi=0
# for i in list1:
#     if i>maxi:
#         maxi=i
# print(maxi)
# mini=int(list1[0])
# for i in list1:
#     if i<mini:
#         mini=i
# print(mini)

# #using tuple
# maxi=0
# for i in tuple1:
#     if i>maxi:
#         maxi=i
# print(maxi)

# mini=int(tuple1[0])
# for i in tuple1:
#     if i<mini:
#         mini=i
# print(mini)

# print(ord('j')) #ascii value to number
# print(chr(65)) #number to ascii value

# sum()

# list1=[69,-85,45,115,48,-87]
# print(sum(list1))
# sum=0
# for i in list1:
#     sum+=i
# print(sum)

# math module
import math
# # math constants
# print(math.pi)
# print(math.e)

# # ceil(),floor() and tunc()
# print(math.ceil(4.6)) 
# print(math.floor(4.9))
# print(math.trunc(3.9))

# print(math.log2(math.e))
# print(math.log(math.e))
# print(math.log10(math.e))

# print(math.sin(0))
# print(math.cos(0))
# print(math.tan(0))

print(math.factorial(5))
print(math.gcd(10,2))
print(math.lcm(10,2))