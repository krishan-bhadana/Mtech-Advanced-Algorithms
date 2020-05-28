#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:20:30 2020

@author: krishanbhadana
"""
def GCD(x,y):
    if(y==0):
        return (x)
    else:
        return (GCD(y,x%y))
x=int(input("Program to calculate GCD\nEnter 1st number"))
y=int(input("Enter 2nd number"))
result=GCD(x,y)
print("GCD is ",result)