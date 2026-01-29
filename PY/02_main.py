#loops in python 
#for loop
numbers= [1,2,3,4]

for i in range(0, 4):
    print(numbers[i])


# for i in range(1):
#     name=input('Enter your name')
    
    

#while loop 
nums= [2,3,4,5,6]
i=0
while(i<len(nums)):
    print(i)
    i+=1
    

#functions
#factorial of a number

def greet():
    print('hello')
    
greet()

def sayHello(name):
    print("hello", name)
    
sayHello("Rahul")


def add(a, b):
    return a+b

ans= add(2,2)
print(ans)

def addition():
    a= int(input("enter number 1: "))
    b= int(input("enter number 2: "))
    return a+b

print("sum is: ",addition())

    
