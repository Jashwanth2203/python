# 1. Positive or Negative: Take a number as input and print whether it’s positive, negative, or zero.
# num1=int(input('enter a number:'))
# if num1>0:
#     print('positive')
# elif num1<0:
#     print('negative')
# else:
#     print('zero')

# 2. Even or Odd: Check whether a number entered by the user is even or odd.
# num1=int(input('enter a number:'))
# if num1%2==0:
#     print('even')
# else:
#     print('odd')

# 3. Largest of Two Numbers: Take two numbers and print which one is greater (or if they are equal). 
# a=int(input('enter first number:'))
# b=int(input('enter second number:'))
# if a>b:
#     print('a is greatest=',a)
# elif a<b:
#     print('b is greatest=',b)
# else:
#     print('both are equal')

# 4. Age Category: Input age and print: Child (<13), Teen (13–19), Adult (otherwise).
# num1=int(input('enter age:'))
# if num1<13:
#     print('child')
# elif num1>18:
#     print('Adult')
# else:
#     print('Teen')

# 5. Divisible by 5 or 11: Check if a number is divisible by both 5 and 11.
# num1=int(input('enter number:'))
# if num1%5==0 and num1%11==0:
#     print('it is divisible by both 5 and 11')
# else:
#     print('it is not divisible by both 5 and 11')

# 6. Leap Year Checker: Check if a given year is a leap year. 
# year=int(input('enter year:'))
# if year%100!=0 and year%4==0:
#     print('it is a leap year')
# else:
#     print('it is not a leap year')

# 7. Pass or Fail: Input marks (out of 100). Print “Pass” if ≥ 40, otherwise “Fail”. 
# marks=int(input('enter marks:'))
# if marks>=40:
#     print('pass')
# else:
#     print('fail')

# 8. Vowel or Consonant: Input a character and check whether it’s a vowel or a consonant.
# str1=str(input('enter character:'))
# list1=['a','e','i','o','u','A','E','I','O','U']
# if str1 in list1:
#     print('it is vowel')
# else:
#     print('it is constant')

# 9. Login System: If username = 'admin' and password = '1234', print “Login successful”, else print “Invalid credentials”. 
# username=str(input('enter username:'))
# password=int(input('enter password:'))
# if username=='admin' and password==1234:
#     print('login successful')
# else:
#     print('invaild credientials')
# 10. Grade Calculator: Input marks and print grade: A (90–100), B (80–89), C (70–79), D (60–69), F (<60). 
# marks=int(input('enter marks:'))
# if marks>=90 and marks<=100:
#     print('Grade A')
# elif marks>=80 and marks<=89:
#     print('Grade B')
# elif marks>=70 and marks<=79:
#     print('Grade C')
# elif marks>=60 and marks<=69:
#     print('Grade D')
# else:
#     print('Grade F')
# 19. Square of Numbers: Print the square of each number from 1 to 10. 
# for i in range(1,11):
#     print(i**2)

# 20. Sum of Digits: Input a number (e.g., 1234) and find the sum of its digits using a loop.

num1=int(input('enter a number:'))
sum=0

while num1>0:
    i=num1%10
    sum+=i
    num1//=10
print('sum=',sum)