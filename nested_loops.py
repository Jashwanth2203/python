# 1■■ Multiplication Table (Nested Loops)
# Write a program to print the multiplication table from 1 to 10 using nested loops.
# for i in range(1,11):
#     for j in range(1,11):
#         print(i,'x',j,'=',i*j)
#     print()
# 2■■ Right-Angled Triangle Pattern
# Print the following pattern using nested loops for n = 5:
# *
# **
# ***
# ****
# *****
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()
# 3■■ Inverted Number Triangle
# Print this numeric pattern:
# 12345
# 1234
# 123
# 12
# 1
# n=5
# for i in range(n,1,-1):
#     for j in range(1,i):
#         print(j,end='')
#     print()
# 4■■ Multiplication Grid
# Display a multiplication grid (matrix style) for numbers 1–5.
# for i in range(1,6):
#     for j in range(i,5*i+1,i):
#         print(j,end=' ')
#     print()
# 5■■ Hollow Square Pattern
# For a given number n, print a hollow square like:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
# n=int(input('enter number:'))
# for i in range(n):
#     for j in range(n):
#         if j==n-1 or j==0 or i==0 or i==n-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# 6■■ Star Pyramid Pattern
# Print the following pyramid pattern for n = 5:
n=int(input('enter number:'))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end='')
    for k in range(1,i+1):
        print('*',end=' ')
    print()