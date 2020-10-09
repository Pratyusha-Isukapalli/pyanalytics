# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 13:43:16 2020

@author: vikas
"""

#List
#Mutable

L1 = [1,2,3,4,5]
L1
type(L1)

#indexed
L1
L1[0]
L1[1]
L1[0:5]

L1[4]

L1[5]

L1[1:4]

L1[:4]

L1[2:]

#Hetrog
L2=[1,"Vikas", 2.3, False, 2.66, "Vikas"]
L2

L2[3]
L2[3:5]



#
for key in L2:
    print(key)
    print(i)
    
#Mutable 
L2[2]=5.50
L2


L2[1].upper()    

L2=[1,"Vikas", 2.3, False, 2.66, "Vikas"]
L2

L2.count("Vikas") 
L2.count(2.3) 

len(L2)   

L2.append("Khullar")
L2

L2.remove("Vikas")
L2

L2.remove("Vikas")
L2

L2.pop()
L2

PopValue=L2.pop(1)
PopValue


del L1[0]
L1

L1.clear()
L1


#copy

L2=[1,"Vikas", 2.3, False, 2.66, "Vikas"]
L2

L1 = L2
L1
L2

L1.pop()
L1
L2

L1 = L2.copy()
L1
L2

L1.pop()
L1
L2

Start = 5
End   = 20
Jump  = 2

a=range(End)
a
list(a)

b=range(Start, End)
b
list(b)

c=range(Start, End, Jump)
c
list(c)

L3=[3,5,2,4,1]

L3.sort()
L3

L4=["Vikas", "Aman", "Shubham"]
L4.sort()
L4

L5=L3+L4

L3.pop()
L5




#L2.remove("Vikas")



#Set Datatype

set = {1,2,3,4,5}
type(set)
set

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1.union(s2)

s1[0]

s1.add(6)
s1.add(4)
s1

s1.add ("Khullar")
s1

s1.add(8)
s1

s1.update([4,9,10,11])
s1

# Dict Ordered
s3 = {3,2,5,1,3}
s3

L3= [3,2,5,1,3]
L3


s4 = ["vikas", "vinay"]

s1
s1.update(["kumar"])
s1
s1.update("kumar")
s1

s1 = {1,2,3,4,5}
s1.remove(1)
s1

s1 = {1,2,3,4,5, "Vikas", "Kumar", "Vikas"}
s1
s1.remove("Vikas")
s1
s1.remove(2)

s1.remove(21)

s1.discard(21)

s1.discard(2)
s1

s1.pop()

s1.pop()
s1

del s1
s1


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = {4,5,6,7,8}

s=s1.union(s2)
s=s3.union(s)
s

s1.intersection(s2)
s1.difference(s2)


#Dict

st = {'rollno': 1}
st
type(st)

st = {'rollno': 1, 'Name': "Vikas", "Educ":"PhD" }
st

st = {'rollno': 1, 'Name': "Vikas", 'Name': "Vinay", "Educ":"PhD" }
st

car  ={'brand':"Honda", 'model': 'Jazz', 'year':2020, 'Purchase': True}
car

car['year']

#car['1']

car.get('brand')

#keys
for i in car:
    print(i)

car.values()

#values
for i in car.values():
    print(i)

len(car)


car  ={'brand':"Honda", 'model': 'Jazz', 'year':2020, 'Purchase': True}

'Jazz' in car.values()

'1brand' in car

#mutable
car['year'] =2019
car

car['Color'] ='Black'
car

L1=[1,2,3]
L1.pop()
L1.pop(0)

S1={1,2,3}
S1.pop()
s1.pop(1)

pop_ele = car.pop('year')
pop_ele

pop_ele = car.pop()


car  ={'brand':"Honda", 'model': 'Jazz', 'year':2020, 'Purchase': True}

car.keys()
car.values()
car.items()


for i in car.items():
    print(i)




for i,j in car.items():
    print("Key ",i)
    print("Value ", j)


#Tupple
    
t1= (1,2,3,4)    

#not mutable
t1[0]
t1[0]=8

for i in t1:
    print(i)


t1=("Vikas", "Aman", "Harman")

if ("Aman1" in t1):
    print("hi")

L1=list(t1)
type(t1)
type(L1)

del t1

#Pending Sting Fns

s1 ="Vikas Khullar Khullar"

s1.replace("Khullar", "Kumar")

s2= "Vikas Khullar"
s3=s2.split(' ')

FName=s3[0]
LName=s3[1]

FName
LName


#Enumerate
L1=["Oranges", "Mangoes", "Apples"]
L1

obj2=enumerate(L1)

L2 = list(obj2)
L2

obj2=enumerate(L1, start =100)

L2 = list(obj2)
L2

obj2=enumerate(L1, start =100)

L2=set(obj2)
L2

obj2=enumerate(L1, start =100)

l3=dict(obj2)
l3

obj2=enumerate(L1, start =100)
for i,j in obj2:
    print(i,j)
    
    
L1 =list(range(100,200))
L1    

obj2=enumerate(L1)

list(obj2)

for i,j in obj2:
    print(i,j)
    if(i==50):
        break
    
for i,j in obj2:
    print(i,j)
    

# Frozenset
#Unmutable Set
    
fs = frozenset([1,2,3])
fs
type(fs)

s1= {1,2,3}
type(s1)
#fs.add(2)
s1.add(5)

b= frozenset ([3,4,5])

fs.add(b)


fs.union(b)
fs.intersection(b)
fs.difference(b)

#zip

name= ["vikas", "Aman", "Ankit"]
roll_no =[1,2,3]
marks = [75,85,73]

z1 = zip(name, roll_no, marks)
type(z1)

s1= set(z1)
s1

z1 = zip(name, roll_no, marks)
l1 =list(z1)
l1

z1 = zip(name, roll_no, marks)

for i,j,k in z1:
    print(i, j, k)




#Multiple remove from List


# list with integer elements
list = [10, 20, 10, 30, 10, 40, 10, 50]
# number (n) to be removed
n = 10

# print original list 
print ("Original list:")
print (list)

# loop to traverse each element in list
# and, remove elements 
# which are equals to n
i=0 #loop counter
length = len(list)  #list length 

while(i<length):
	if(list[i]==n):
		list.remove (list[i])
		# as an element is removed	
		# so decrease the length by 1	
		length = length -1  
		# run loop again to check element							
		# at same index, when item removed 
		# next item will shift to the left 
		continue
	i = i+1

# print list after removing given element
print ("list after removing elements:")
print (list)
