# # for inside for
# for i in range(5):
#     for j in range(8):
#         print('*',end=' ')
#     print()

# # while inside while
# i=0 
# while i<=3:
#     j=0
#     while j<=5:
#         print('*',end=' ')
#         j+=1
#     print()
#     i+=1
    
# # for inside while
# for i in range(5):
#     j=0
#     while j<=8:
#         print('*',end=' ')
#         j+=1
#     print()

#  #  while inside for
# i=0 
# while i<=3:
#     for j in range(8):
#         print('*',end=' ')
#     print()
#     i+=1
    
for i in range(1,8):
    for j in range(1,i+1):
        print(j,end=' ')
    print()