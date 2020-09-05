# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a=10
b=20
a+b

#print?

print("Pratyusha","Isukapalli",a, sep="_", end="_UM20216\n")
print("I am studying MBA BM at XIMB", end="\n")

help(print)

help("OPERATORS")

import pandas as pa

'''
!pip install pandas
!python --version
!pip list
'''

input("Your Country ")

a="Pratyusha"
b=10
c=30.5

type(c)

s = input("My name is pratyusha")
type(s)

#Type casting
Number = int(input())
print(Number)
type(Number)

Num = float(Number)
print("The type is", type(Num))

country = "India"
countrycode = 91
print("Pratyusha", str(country))
print("I live in {0} which is a very good country, whose country code is {1}".format(country,countrycode))

a=1.11
b=int(a)
c=float(b)

type(a)
type(b)
type(c)


x=2
y=3
z=x+y
print(z)

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)

x=x-1
x

x-=1
x

x*=2
x

x**2
x**3

a=10
b=11

a/2
b/2

b%2

#boolean
0-9

'''
Multiple line comments
Booleab operators
'''

A=True
B=False

x = A and B
print(x)


A=0
B=0

x = A and B
print(x)

A=True
B=False

x = A or B
print(x)


A=0
B=1

x = A or B
print(x)

A=0
B=1

x = not(A or B)
print(x)
'''
boolean operator done
'''

#Bitwise operator

A=0
B=1

x = A & B
print(x)

A=000
B=110

x = A | B
print(x)

#Bitwise operator done!

#string concatenation
FName = "Pratyusha"
LName = "Isukapalli"

name = FName +" "+ LName+"_"+str(20216)
print(name)

#length of the string
len(name)

#Capitalize
LName.capitalize()

#UPPER
name.upper()
print(name)

#lower
name.lower()
print(name)

#append
name.rjust(35,'*')
name.center(35, '*')
name.ljust(35, '*')

#replace
name.replace("20216","UM20216")
