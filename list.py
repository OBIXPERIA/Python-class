"""
List - list is a type of variable that allows you store mutiple items together and access them using their index

Note : the index starts from 0 

LIST STRUTURE
list_name = []
        or
list_name = list(1,23,4,5,3)


LIST METHODS - are built-in functions you can use to manipulate a list

1. append
2. extend
3. pop
4. insert
5. remove
6. copy
7. count
8. index
9. reverse
10. sort
"""


list1 = [1,23,4,5,5]
list2 = list('swd')


# append - adds new item to the back of the list
list1.append(25)


# extend - joins two list together
list1.extend(list2)


# pop - deletes the last kitem in an list
# list1.pop()

# reverse - display items from the last
list1.reverse()

# insert- adds item to a specific index (index_position, item)
list1.insert(1,'heloo')

#count - returns the occurance of an item in a list (item) 
print(list1.count(5))


# index - returns the index position of an item in a list (item)
print(list1.index(4))


# remove - deletes item in a list (item_name)
list1.remove(23)


# sort - sort list
sort_list = [4,5,6,1,2,3]

sort_list1= sort_list.copy()
sort_list1.sort(reverse=True)
# sort_list1.append(10)
print('sort list 1: ',sort_list1)

# copy -
sort_list2 = sort_list.copy()
sort_list2.sort(reverse=False)
print('sort_list2:', sort_list2)

print('orignal list',sort_list)

# print(list1)
