# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 19:39:22 2020

@author: isuka
"""

import random

x = random.randint(1,10)
print(x)

#### Random number from a defined list
li = [11,1,23,28,35,14,18]
random.choice(li)

list1 = random.choices(li,k=3) ## Choose random list
print(list1)

# For dict and sets change them into list to have multiple random values
dic = {"Name":"Pratyusha","RollNo":28,"Course":"Python"}
random.choices(list(dic),k=1)

## Alias name for imported variables
import random as rd
rd.choices(li, k=3)

movie_list = ["Mv1","Mv2","Mv3","Mv4","Mv5"]
rd.choice(movie_list)
random_index = rd.randrange(len(movie_list))##To get random number index 
print(random_index)

###############   seed



###############   numpy
import numpy as np

np.random.randint(1,10)
np.random.randint(10,1000,size=10) ## The range should contain only one type

arr=np.random.randint(10,100,size=(4,4))
arr

arr.shape

arr[0,0]
arr[0,1]
arr[1,0]
arr[1,1]

arr[0,0:3]
arr[:,0:3]
arr[:,2:]

arr[2:4,1:3]

arr[-2:-1,:]

arr[-2:,-2:]

arr[2:,2:]

########## arange
np.arange(10)
arr1 = np.arange(10,20)
np.arange(10,20,2)
arr1.shape


########## Reshape
arr1reshape = arr1.reshape(2,5)
arr1reshape

arrireshape = arr1.reshape(10,1)
arrireshape

arr2reshape = arr1.reshape(1,10)
arr2reshape

np.zeros((2,4))
np.ones((2,8))

np.zeros((2,4), dtype='int32')
np.ones((2,8), dtype='int32')

#######skeleton array
arr5 = np.empty((4,5))
arr5

np.eye(3,3) ###Identity matrix

np.linspace(0,4)
np.linspace(0,12,num=4)
np.linspace(0,12,num=4,dtype='int32')