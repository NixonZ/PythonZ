# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:42:43 2018

@author: Nalin Shani
"""

A=[]
x=''
while 1:
    temp=input("Enter a number to add to the array(type 'exit'to quit)\n")
    if temp=='exit':
        break
    A.append(int(temp))
B=[temp for temp in A if not(temp%2)]
print(B)