# enumerate function

# fruits=['apple','mango','orange','papaya','muskmelon']

# for ind,fruit in enumerate(fruits,start=101):
#     print(ind,fruit)
# print(list(enumerate(fruits)))
# print(dict(enumerate(fruits)))

# for ind,fruit in enumerate(fruits,start=101):
#     if fruit=='apple':
#         print(f'index of {fruit} is {ind}')

# students=['viswa','jashwanth','swaroop','samuel','sai kiran']
# print(dict(enumerate(students)))

# details={'name':'jashwanth','place':'hyderabad','contact':9121385460}
# print(dict(enumerate(details.values())))

# zip function

students=['viswa','jashwanth','swaroop','samuel','sai kiran']
marks=[85,56,45,23,78]
departments=['cse','csm','eee','ece','it']
# print(list(zip(students,marks)))
# print(list(zip(students,marks,departments)))

# for student,mark,department in zip(students,marks,departments):
# print(dict(zip(students,zip(marks,departments))))
    
dict1={}
for i in range(len(students)):
    dict1=[students[i]==marks[i],departments[i]]
print(dict1)

