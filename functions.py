# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:01:54 2020

@author: isuka
"""
############################### FUNCTION ##################################
a=10
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

## Function is recognised by () at the end and def at the beginning

## with parameters and without return type
def opera (a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a**b)
    
##Calling the function
opera(5,2) 

## with parameters and with return type
def addFun(a,b):
    return a+b

c = addFun(5,2)
print(c)

## Factorial ##

def fact(num):
    i=num
    fact=1
    while(i>=1):
        fact=fact*i
        i=i-1
    return fact

fact = fact(4)
print(fact)

## Function with multiple return type ##
def ope(a,b):
    Sum = a+b
    dif = a-b
    return(Sum,dif)   

print(ope(5,2))
a, b = ope(5,2)
type(a)
type(b)
c = ope(5,2)
type(c)

## string return type
def printHello(fName,lName):
    print("Hello "+fName+" "+lName+", welcome to PYTHON class!!")
    
printHello("Pratyusha","Isukapalli")

