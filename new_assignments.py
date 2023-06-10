# Q 2 write a programme to sum all the items
sum_list=[1,2,3,4,5]
add=0
for item in sum_list:
  add=item+add
print(add)

# Q 3 write a python programme to get the largest no from the list
large_list=[10,20,30,100,40]
large_list.sort()
print(large_list[-1])

# Q4 write a python programme to get the largest no from the list
small_no=[-1,1,2,3,2,5,-2,7]
small_no.sort()
print(small_no[0])

# Q 7 write a python program to insert a given  string at the begining of all the items in a list
insert_list=[1,2,3,4]
str_insert=('emp')
dummy=[]
dummy1=[]
for item in insert_list:
  dummy1=str_insert+str(item)
  dummy.append(dummy1)
print(dummy)

# Q 6 Write a python programme to check a list is empty or not
empty_list=[]
empty_list==[]

