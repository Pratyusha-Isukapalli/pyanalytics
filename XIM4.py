# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:03:49 2020

@author: vikas
"""


#Functions
#Block of code which only runs when it is called
#can pass data, known parameters into function
#it can return data as result
#defined using keyword def with colon :


a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

a=20
b=30
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)


a=50
b=60
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)


a=70
b=40
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)


#user defined functions
def oper(a,b):
    print("Sum", a+b)
    print("Sub", a-b)
    print("Mul", a*b)
    print("Div", a/b)
    print("Pow", a**b)
    

oper(10,20)

oper(30,50)


i=1
j=1

while(i<10):
    print("Oper Call")
    oper(i,j)
    i=i+1
    j=j+1
        

def oper(a,b):
    Sum= a+b
    Sub= a-b
    return(Sum, Sub)


a, b = oper(10,20)
type(a)

c= oper(10,20)
type(c)
    

def printhello(fname):
    print("Hello", fname, "     welcome")
    

printhello("Aman")
printhello("Sushant")



def totalsale(x, y):
    return(x+y)

totalsale()


def totalsale(x=0, y=0):
    c=x+y
    return(c)

totalsale()

totalsale(10,20)



#random numbers

import random

x = random.randint(100,1000)
x


l1= [11,12,13,14,15,16]

random.choice(l1)


import random
st = "abcdef"
st
random.choice(st)

names=["vikas", "Aman", "Simar", "Sirat"]

random.choice(names)

random.choices(names, k=2)

L1 =random.choices(l1, k=3)
L2 =random.choices(l1, k=3)
L3 =random.choices(l1, k=3)
L4 =random.choices(l1, k=3)

L1
L2
L3
L4


import random
sample= random.choices(names, k=2)

sample


d1= {"Name": "vikas", "RollNo": 111, "Class": "ML" }
type(d1)
d1
c= random.choices(list(d1), k=3)
c

s1={20,30,40,50}

c= random.choices(tuple(s1), k=3)
c

c= random.choices(list(s1), k=3)
c


import random as rd
rd

rd.choices(list(s1), k=3)


movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']

rd.choice(movie_list)

random_index = rd.randrange(len(movie_list))

item = movie_list[random_index]

print ("Randomly selected item and its index is - ", item, 
       "Index - ", random_index)

s1={1,2,3,4}
l1=list(s1)
l1[2]

t=(1,2,3,4)
t[1]

d1={"A":1, "B":2}
l1=list(d1)
l1

l1Values=list(d1.values())
l1Keys =list (d1.keys())

l1Values
l1Keys

















#4 groups of 5 random numbers


l1=[]
l2=[]
l3=[]
l4=[]

i=0

while(i<4):
    l1.append(random.randint(100,1000))
    l2.append(random.randint(100,1000))
    l3.append(random.randint(100,1000))
    l4.append(random.randint(100,1000))
    i=i+1

l1
l2
l3
l4































    
    
    
