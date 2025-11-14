'''x = 10
if x >= 10:
    print("x is greater than or equal to 10")
    if x > 20:
       print("x is greater than 20"   )
    else: print("x is not greater than 20")


x = int(input("Enter the number"))
if x % 2==0:
    print("x is even")
else: print("x is odd")    


age = int(input("enter the age"))
if age >=18:
    print("You are eligible for driving")
else : print("You are not eligible for driving")    


fruits = ["apple","banana","cherry"]
for x in fruits:
  print(x)

word = "python"
for x in word:
   print(x)

for i in range(5):
    print(i)

for i in range(1,10,2):
    print(i)    

for i in range(1,4):
    for j in range(1,3):
        print(f"i ={i},j={j}")

for i in range(1,6):
    if i == 4:
        break        
    print(i)

for i in range(1,6):
    if i == 4:
        continue      
    print(i)    

for i in range(1,21): #1st question
    print(i)    


for x in range(1,31): #2nd question
    if x % 2==0:
     print(x)    

list = ["black","white","pink"] #3rd question
for x in list:
 print(x)

for i in range(1,11):
        print(f"3*{i}={3*i}") 


for i in range(1, 4):   #4th question
    for j in range(1, 4):      
        print(i * j, end="\t") 
    print()                    


def a():
    print("hello, python")

a()    

def great(name):
    print(f"hello,{name}")

great("bob")
great('alice')

def add(a,b):
    return a+b

a = add(5,9)
print(a)

def multiply(a,b):
    return a*b

a = multiply(5,9)
print(a)

def divide(a,b):
    return a/b

a = divide(5,9)
print(a)

def subtract(a,b):
    return a-b

a = subtract(5,9)
print(a)

def greet(name="student"):
    print(f"Hello,{name}")

greet()
greet("Alice")

x=10
def my_func():
    y = 5
    print("inside",x,y)

my_func()
print("Outside",x)
#print(y) 

def greet():     #1st question
    print("Hello")
greet()

def add(x,y):    #2nd question
    return x+y
z = add(5,9)
print(z)


#3rd question
a=7 #a is global variable  
def my_func():     
    b = 12 #b is local variable
    print("inside",a,b)

my_func()
print("Outside",a)
#print(b)  #this will throw an error that b is not defined as it is local variable.

class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def drive(self):
        print(f"{self.color}{self.brand}is driving🏎️")

car1 = Car("Mercedes G-Wagon","Black")
car2 = Car("Buggati Chiron","White")       

car1.drive()
car2.drive()

import array

numbers = array.array("i",{1,2,3,4,5})
print(numbers)

from numpy import random
x=random.randint(100)
print(x)

x = random.rand()
print(x)
print(type(x))

[34]
[1,2,3,4,5]
[[1,2,3],
 [4,5,6]]


[[[1,2,3],
 [4,5,6]]
[[7,8,9],
 [10,11,12]]]'''


from numpy import random
#x = random.randint(100,size=5) #1d array
#print(x)


#x = random.randint(100,size=(3,5)) #2d array
#print(x)

#x = random.randint(100,size=(2,3,5)) #3d array
#print(x)


#x = random.randint(100,size=(2,2,3,5))  #4d array
#print(x)

#x = random.choice([3,5,7,9])
#print(x)

#x = random.choice([4,5,6],size=5) #1d array
#print(x)

#x = random.choice([4,5,6],size=(2,3,5)) #3d array
#print(x)

import pandas as pd
'''data = [10,20,30,40]
x = a.Series(data)
print(x)

data1 = {"Name":["Alice","Bob","Charlie","David"],
         "Age":[24,27,22,32],
         "City":["Delhi","Mumbai","Chennai","Kolkata"]
         }
df = a.DataFrame(data1)
print(df)'''

import numpy as np
a = np.array([1,2,3,4])
b = pd.Series(a)
print(b)

data = {"Math":90,"Science":86,"English":78}
a = pd.Series(data)
print(a)

df = pd.read_csv("D:\Downloads\crocodile_dataset.csv")
print(df.head())
print(df.tail())















    






    
