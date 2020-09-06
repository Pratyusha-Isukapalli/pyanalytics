# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:55:06 2020

@author: isuka
"""

############################### CONDITION #################################
# !=, ==, <=, >=, <, > comparision operators
###### if condition
'''
if (condition):
    statement1;
    statement2;
    ....
    
'''

a = 10
if (a<=10):
    print("True, a is <= 10")

b = True
if(b):
    print("Yes, it is true")
    
num1 = 10
num2 = 20
if(num1<=num2):
    print("condition satisfied")

###### if-else condition
age = 18
if(age>=18):
    print("A major")
else:
    print("A minor")
    
###### if-else if
marks = 70
if(marks>80):
    print("Distinction")
elif(marks>70 and marks<=80):
    print("First class")
elif(marks>60 and marks<=70):
    print("Second class")
else:
    print("Fail")
    
################################# LOOP ###################################

team = ["India","Indonesia","Australia","USA"]
for i in team:
    print(i)
    
teamLength = len(team)
teamLength

for i in range(teamLength):
    print(team[i])
    
for i in range(10):
    print(i)
    
ran1 = range(1,10,2) ### start, end, jump
for i in ran1:
    print(i)

ran2 = range(1,5)
for i in ran2:
    print(i)
    
for i in range(len(team)):
    print(team[i])

team1 = ["India","Australia","USA"]
team2 = []
for i in range(len(team1)):
    team2.append(team[i])
team2

for i in range(len(team1)):
    team1[i]=team1[i]+"_A"
print(team1)
team1

x="USA"
for i in team1:
    if i == x:
        print("The team is present")
        break
    else:
        print("The team is not present")

####while
i=0
while (i<10):
    print(i)
    i+=1
  
###break
i=1
while (i<10):
    print(i)
    if(i==5):
        print("exiting the loop")
        break
    i+=1
    
###continue
i=0
while (i<10):
    
    i+=1
    if(i==5):
        continue
    print(i)
    
    