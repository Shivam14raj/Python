# int to float

x=10
print(x) #10
y=float(x)
print(y) #10.0
print(type(y))

# float to int 
p=10.9
q=int(y)
print(type(q))
print(q)


#boolean
a=5 
print(a)
b=4
print(a==b) #false



#special data types in python

# python has two objects: immutable and mutable 
#immutable: int, float, string, bool, tuple, 
#mutable: list, set, dictionary 

#List should be included in []

my_list = [1,2,3, "apple", True] # can have multiple data types
print(my_list)
print(type(my_list))

my_list.append("mango")
print(my_list)

print(my_list[3]) # printing using index value like array

print(len(my_list))


del my_list[0] 
print(my_list)

#join two list
my_list2= [1,2,3,4,5,6,7,8,9]

add_list= my_list+ my_list2
print(add_list)

#Tuple(immutable data type)
# allows multiple data types 

tuple_1= (2,3,4, 'mango', False)
print(tuple_1)
print(type(tuple_1))

print(tuple_1[1]) 

#set (mutable)
mySet= {1,2,3,3 } #only similar data type (does not support indexing)
print(mySet) # 1,2,3 
mystring={"apple","mango"}
print(mystring) 

#converting list into set
mylist= [1,2,3,3]
print(mylist) #1,2,3,3
listToSet= set(mylist)
print(listToSet) # 1,2,3

#dictinoary
# key-value pair 
myDict= {'name':'Rahul', 'age':23, 'age': 20} #age is overwritten 
print(myDict)
print(type(myDict))

print(myDict['name'])
print(myDict['age'])

# set and dictinoary does not allow duplicate value but list and tuples does

