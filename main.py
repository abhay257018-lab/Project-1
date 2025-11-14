print("Hello World")

mylist = [1,2,3,4,5,6]

mylist.append("apple")



print(mylist)

mylist.append('xyz')
print(mylist)

mylist.remove("apple")
print(mylist)

mylist.pop()
print(mylist)

mylist.clear()
print(mylist)

list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1)

list1.remove(6)
print(list1)

list1.pop()
print(list1)

list0 =[]
list0.append(1)
print(list0)

list0[0]='hello'
print(list0)

list2 = [1,2,3,4,4,4,5,6]
for x in list2:
    print(x)

list3 = [2,5,18,1,4,8,29,16,3,6,12,19,25,21,7,23,10,27,14,22,26,9,17,13,28,30,11,24,20,15] #sort 1 to 30
list3.sort()
print(list3) 
list3.sort(reverse=True)
print(list3)    

text = "hello"
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("hello","e"))
print(text.split())

#x = 5
#y = "hello"
#print(x+y)

x = "bob"
y = 20
print(f"my name is {x} and my age is {y}")


x = 20
x *= 4
print(x)
x /= 6
print(x)
x -= 8
print(x)
x += 19
print(x)

y = 2
y **= 4
print(y)
y %= 5
print(y)

y = 12
y //= 6
print(y)

a = 5
b = 10
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a<b)
print(a>b)

x = 5
y =x
print(x is y)
z = 10
print(z is x)
print(z is not x)

students = {"name":"chander","age":30,"grades": "A"}
print(students)

age = 17
if age>=18:
    print("you are an adult")
elif age ==17:
    print("You are not an adult")

else : print("you are not an adult")    

marks = 85
if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else : print("Grade D") 

x = 15
if x > 10:
    print("x is greater than 10")
    if x > 20:
       print("x is greater than 20"   )
    else: print("x is not greater than 20")    
