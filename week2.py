#creating an empty list
my_list = []
print(my_list)

#appending elements
my_list = []
my_list.append (10)
print('after append:', my_list)

my_list = [10]
my_list.append (20)
print('after append:', my_list)

my_list = [10,20]
my_list.append (30)
print('after append:', my_list)

my_list = [10,20,30]
my_list.append (40)
print('after append:', my_list)
#appending one element at a time

#insert value 15 at 2nd 
my_list = [10,20,30,40]
value_to_insert = 15
my_list.insert(1, value_to_insert)
print(my_list)

#extending my_list with another list
my_list = [10,15,20,30,40]
print('list1:', my_list)
another_list = [50,60,70]
print('list2:', another_list)
my_list.extend(another_list)
print('list after extend:',my_list)

#remove last element from list
my_list = [10,15,20,30,40,50,60,70]
del my_list[7]
print(my_list)

#sort in ascending order
my_list = [10,15,40,30,20,50,60]
my_list.sort()
print(my_list)

#find and print index value 30
my_list = [10,15,20,30,40,50,60]
print(my_list[3])

#assignment for week2 on python
