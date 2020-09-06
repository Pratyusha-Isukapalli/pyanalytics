# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:11:48 2020

@author: isuka
"""
#############################   LIST   #################################
#List elements - Homogenous data types
#Mutable - Allows to add variables anytime

L1 = [1,2,3,4,5]
type(L1)

####LIST gives INSERTION order#####

#Indexed List
print(L1[0])
print(L1[0:3])
print(L1[2:]) #From index 2 
print(L1[:3]) #Till index 3
print(L1[6])  #Index out of bound exception

#List elements - heterogenous data types
L2 = [518,"Pratyusha",97.9,True]
print(L2)
type(L2)

#Mutable - can be changed
L2[1] = "Isukapalli"
L2[0] = "Pratyusha"

#Length of the list
len(L2)

#List with for loop - For printing the list elements
for i in L2:
    print(i,type(i))
    
#Remove elements from the list
L2.remove(True)
len(L2)

#Identifies no. of objects present
L2.count("Pratyusha")

#Append - Mutable - Adding the object to the list through append
L2.append(True)
print(L2)

#Deletes the first occurence
L3 = ["Pratyusha",518,97.7,"Pratyusha"]
L3.remove("Pratyusha")
print(L3)

#pop() Removes the last element from the list - LIFO
L3.pop()    #Removes "Pratyusha" as it is the last element

#del L[0] - Deletes the specific element from the list
del L3[0]
print(L3)

#It just creates a reference which reflects all the changes done to the L3
L = L3
print(L)

#L.copy(L3) used to make a copy of the existing element - Two different references - Not dependent on each other.
L=L3.copy()
L.pop()
print(L)
print(L3)

#range function - usage with the list - range(start,end,jump)
start = 0
end = 10
jump = 3

a = range(end) #By default starts from 0 and ends at end 10
a
list(a) # start to end-1

b = range(start,end)
b
list(b)

c = range(start,end,jump)
c
list(c)

#sort function - numbers and integers - not supported
L3.sort()
print(L3)

#sort function - Strings/Integers
li1 = [14,28,18,35]
li2 = ["Pratyusha","Tunir","Siddanth","Ankana","Ananya"]
li1.sort()
print(li1)
li2.sort()
print(li2) 

#Concatenate two lists
li3 = li1 + li2
print(li3)

############################## SET ##################################

set1 = {1,2,3,4}
type(set1)
print(set1)

set2 = {5,6,7,8}
type(set2)
print(set2)

#UNION - gives the elements after removing duplicate values common in both the sets
set1.union(set2)

set1[0] = "10" #'set' object does not support item assignment

#add - to add new elements in set
set1.add(6)
print(set1)

set1.add(4) #set doesn't allow the duplicate values
print(set1)

set1.add("Pratt") #set is heterogenous
print(set1)

set1.add([10,11,12]) #unhashable type: ''''list'''' ******ERROR******

#update - to update the existing element in the specified location
set1.update("Pratyusha") #Adds this as seperate characters
print(set1) #{1, 2, 3, 4, 'y', 6, 'u', 'h', 'r', 'P', 'Pratt', 's', 't', 'a'}

set1.update(["Pratyu","tyyu"])

#####SET gives ORDERED Outcome###### Dictionary based sorting for strings
s1 = {4,7,2,3,0}
print(s1) # {0, 2, 3, 4, 7}
print(s1[0]) ###'set' object is not subscriptable '[0]' ********ERROR*******

#REMOVE
set1.remove(2)
print(set1)
set1.add(2)
set1.add(3)

set1.update(["Pratyusha","Pratt","Pratyu"])
set1.remove(20) ###Value not existing *****ERROR*****

######DISCARD######
set1.discard(20) #No ERROR

#POP
set1.pop() #####POP the element from the beginning
print(set1)

set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,10}

set1.union(set2)
print(set1)

#INTERSECTION
set1.intersection(set2) #Gives the common elements set as output

#DIFFERENCE
set1.difference(set2) #Gives the elements present in set1 excluding the elements from set2

############################## DICTIONARY ###############################

# Dictionary - a key and a value pair
# Duplicate keys are not allowed
student = {'rollno':20216,'name':'Pratyusha', 'course':'BM'}
print(student)
student.keys()
student.values()

#Fetch the values and keys
#Method1
student.get('rollno')
student.get('name')
student.get('course')
#Method2
student['name']
#Method3
#Keys
for i in student:
    print(i)
    #Values
for i in student.values():
    print(i)
#Method4
#Check with true/false
'rollno' in student #Returns boolean, if the key or value is existing
'Pratyusha' in student.values()

###### MUTABLE #######
student['rollno'] = 216
print(student)

###### POP #######
pop_ele = student.pop('course')
print(pop_ele)

student.items()

for i in student.items():
    print(i)
    
for i,j in student.items():
    print("key is   ",i)
    print("value is ",j)

############################# TUPLE #################################

######UNMUTABLE
t1 = (1,2,3,4)
print(t1[0])
t1[0]=5 ##'tuple' object does not support item assignment ****ERROR****

for i in t1:
    print(i)
    
t2 = ("Pratyu", "Pratt", "Pratyusha")
"Pratyu" in t2 #Returns true/false

if("Pratyusha" in t2):
    for i in t2:
        print(i)

List1 = list(t2)
type(List1)
print(List1)

t1.remove() ## -- 'tuple' object has no attribute 'remove' IMMUTABLE

del t1 ## -- can delete complete tuple, but not single element


############################ String ####################################

###REPLACE
str1 = "Pratyusha Isukapalli"
str1.replace("Pratyusha", "Pratyu")

###SPLIT
str2 = "Pratyusha Isukapalli"
strList = str2.split(" ")
print("First name is::",strList[0])
print("Last name is::",strList[1])

############################# ENUMERATION ###############################
enuList = ["eat","sleep","repeat"]
enuObje = enumerate(enuList,start = 100)
type(enuObje)
print(enuObje)
enuList1 = list(enuObje)
print(enuList1)
print(type(enuList1))

enuLi = ["Apple","Orange","Mango"]
enuOb = enumerate(enuLi) #### DEFAULT start = 0
print(type(enuOb))
enuLi1 = list(enuOb)
print(enuLi1)
print(type(enuLi1))

enuset1 = set(enuOb)
print(enuset1)
print(type(enuset1))

enudic1 = dict(enuOb)
print(enudic1)
print(type(enudic1))

for i in list(enuOb):
    print(i)

######################### FROZENSET ####################################

fs1 = frozenset([2,3,4,5])
fs1

fs2 = frozenset([5,6,7,8])
fs2

fs1.union(fs2)
fs1.intersection(fs2)
fs1.difference(fs2)

######################### ZIP ############################################

name = ["Pratyusha","Pratyu","Pratt"]
rollNo = [1,2,3]
marks = [75,85,45]

z1 = zip(name,rollNo,marks)
type(z1)

z1 = zip(name,rollNo,marks)
zset1 = set(z1)
zset1

z1 = zip(name,rollNo,marks)
zlis1 = list(z1)
zlis1

z1 = zip(name,rollNo,marks)
for i in z1:
    print(i)

z1 = zip(name,rollNo,marks)
for i,j,k in z1:
    print(i,j,k)
    
