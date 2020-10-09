# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 20:40:23 2020

@author: vikas
"""


import numpy as np

np.random.randint(100, 1000)

np.random.randint(100)

#similar type of data
arr=np.random.randint(10, 1000, size=10)

arr[-2:]
arr[:-2]

#indexed accessable
arr[1]

#mutable
arr[2]= 200

arr

arr=np.random.randint(1, 9, size=(5,4))
arr

arr[0,0]
arr[0,1]
arr[0,2]
arr[0,3]

arr[1,0]
arr[1,1]
arr[1,2]
arr[1,3]



arr
arr[0,0:3]
arr[:,0:2]
arr[:,2:4]

arr[2:4,1:3]

arr
arr[-2:,-2:]




range(0,10, 2)


np.arange(10)
np.arange(10, 20)
arr1= np.arange(10, 20)

arr1.shape
arr1
arr1reshape= arr1.reshape(2,5)
arr1reshape
arr1reshape.shape

arr2reshape= arr1.reshape(5,2)
arr2reshape
arr2reshape.shape


arr3reshape= arr1.reshape(2,5)
arr3reshape
arr3reshape.shape





arr1= np.arange(10, 22)

arr1.shape
arr1

arr1reshape= arr1.reshape(2,6)
arr1reshape
arr1reshape.shape

arr2reshape= arr1.reshape(6,2)
arr2reshape
arr2reshape.shape


arr3reshape= arr1.reshape(4,3)
arr3reshape
arr3reshape.shape




a=np.zeros((2,4))
a

a = np.ones((2,4))
a
a = np.ones((2,4), dtype='int16')
a


b=np.ones((2,4), dtype="int32")


a+b
a*b



l1=[]

l1.append(2)


#np.random.randint(10.0, 100.0)
#np.random.random(10)

#arr6.append([2])

arr5 = np.empty(1)
arr5.shape


np.eye(4,2)


import numpy as np

arr=np.linspace(1, 12, num=4, dtype="int32")
arr

l1= [1,2,3,4]
type(l1)

a=np.array(l1)

type(a)


a1= np.array([1,2,3,4,5])
a1


a1=np.arange(10)
a1

a1 = np.array([2,3,1,4,5])

a1.sort()

a1

a1=a1[::-1]

a1

#reverse order

np.sort(a1)

l1= [1,2,3,4,5]

l1

LR=l1[0:3]
LR

lR= LR[::-1]

lR

np.sort(a1)


arr3= np.random.randint(1,10, size=10)
arr3.sort()
arr3=arr3[::-1]
arr3

arr3  = np.array([5,6,7,8,1])
arr3  = np.sort(arr3)
arr3
arr3.sort()


np.mean(arr3)
np.std(arr3)


a=np.random.normal(100,10,100)
a.mean()
a.std()
a
a.round(2)
arr = np.floor([12.5,67.8])
arr = arr.dtype("int32")

np.floor([-12.5,67.8])
np.ceil([-12.5,67.8])
np.trunc([-12.5,67.8])

a.mean()
a.std()

name=np.array(['Vikas', 'Aman', "Joseph", 1, 1.0])
name

name.shape

x4= np.array([1,2,3,4])
x5 = np.array([7,8,9,0])

x4.shape

x4a=np.concatenate([x4,x5])
x4a

x= np.arange(6).reshape(2,3)
x

y=np.arange(6,12).reshape(2,3)
y

np.concatenate([x,y], axis = 0)

np.concatenate([x,y], axis = 1)



x= np.arange(6).reshape(2,3)
x

y=np.arange(6,12).reshape(3,2)
y

np.concatenate([x,y], axis = 0)
np.concatenate([x,y], axis = 1)

x.shape
y.shape

x= np.arange(10,22)
x

x1=np.split(x,3)

x1[0]
x1[1]
x1[2]

x2=x.reshape(4,3)
x2

x3= np.vsplit(x2,[2])

x3

x4 = np.hsplit(x2,[2])
x4


x2
x2+5

x2*5

np.add(x2,5)
np.multiply(x2,5)

x2
np.mean(x2)
np.median(x2)
np.sum(x2)
np.min(x2)
np.max(x2)

import numpy as np
x= np.random.randint(30,50, size=20)
x.shape
x
np.median(x)

np.equal(x,36)


text = np.array(['Vikas', 'Raman', 'Amit'])
np.equal(text, "Vikas")

x
np.greater(x,36)
np.less(x,36)

np.greater_equal(x, 36)
np.less_equal(x,36)

x

np.all(x <= 29)


x
x>35

np.sum(x>35)


x = np.random.randint(12, size= (3,4))
x

np.sum(x>6, axis=0)

np.sum(x>6, axis=1)

np.sum(x>6)


















