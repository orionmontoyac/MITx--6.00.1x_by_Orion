# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:45:47 2017

@author: Orion
Problem set 2
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print:
Number of times bob occurs is: 2

"""

s = 'azcbobobegghaklbobob'
num = 0  
for i in range(len(s)):
    if s[i] == 'b':
        if s[i:i+3] == 'bob':
            num+=1
print(num)
    