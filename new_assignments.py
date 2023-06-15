# Q 1 Write a python programme that initialises non empty list of words with length=5. Display longest word with its length.
sample_list=['mango','banana','kiwi','apple','grapes']
large=("")
for char in sample_list:
  if len(char)>len(large):
    large=str(char)
print(large)
print(len(large))

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

# Q 5 write a python programme to count the no. of strings where the string length is 2 or more and the first and last char are same from a given length of strings.
sample_list=['abc','xyz','aba','1221','3443']
count=0
for char in sample_list:
  if len(char)>=2 and char[0]==char[-1]:
    count=count+1
  

print(count)

# Q 6 Write a python programme to check a list is empty or not
empty_list=[]
empty_list==[]
   

# Q 7 write a python program to insert a given  string at the begining of all the items in a list
insert_list=[1,2,3,4]
str_insert=('emp')
dummy=[]
dummy1=[]
for item in insert_list:
  dummy1=str_insert+str(item)
  dummy.append(dummy1)
print(dummy)

# Write a program that takes a string as input and counts the number of vowels(a,e,i,o,u) using for loop
i=0
for char in str:

  if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    i=i+1
print(i)

# Write a program that takes a string as input and counts the number of vowels(a,e,i,o,u) using for loop
str=('the quick brown fox jumps over the table')
i=0
for char in str:

  if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    i=i+1
print(i)

#Write a program that generates all possible combinations of three numbers from 1 to 5 using nested for loops and print the
for i in range(1,6):
  for i2 in range(1,6):
    for i3 in range(1,6):
      print(i,i2,i3)