#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28:28:37 2020

@author: krishanbhadana
"""
def entermatrix(size):
    T=[[0 for w in range(size)] for t in range(size)]
    for i in range(size):
        for j in range(size):
            T[i][j]=int(input("Enter "+str(i)+" row and "+str(j)+" column "))
    return T
    
def caluppertriangularmatrix(T): 
    if (T[1][0]==0 & T[2][0]==0 & T[2][1]==0):
        return(1)
    else:
        return(0)
        
def callowertriangularmatrix(T): 
    if (T[0][2]==0 & T[0][1]==0 & T[1][2]==0):
        return(1)
    else:
        return(0)

def inverse(X):
    I=X
    uppert=caluppertriangularmatrix(I)
    lowert=callowertriangularmatrix(I)
    if(uppert==1 & lowert==1):
        return(X)
    elif(uppert==0 & lowert==0):
        print("Inverse cannot be calculated using this method")
    elif(uppert==1 & lowert==0):
        I[0][1]=0-X[0][1]
        I[1][2]=0-X[1][2]
        I[0][2]=0-X[0][2]-(X[0][1]*I[1][2])
        I[0][0]=1/X[0][0]
        I[1][1]=1/X[1][1]
        I[2][2]=1/X[2][2]
        I[1][0]=0
        I[2][0]=0
        I[2][1]=0
    elif(uppert==0 & lowert==1):
        I[1][0]=0-X[1][0]
        I[2][0]=0-X[2][0]-(X[2][1]*I[1][0])
        I[2][1]=0-X[2][1]
        I[0][0]=1/X[0][0]
        I[1][1]=1/X[1][1]
        I[2][2]=1/X[2][2]
        I[0][2]=0
        I[0][1]=0
        I[1][2]=0
    return(I)
   
print("\nEnter a 3X3 matrix")
X=entermatrix(3)
Y=inverse(X)
print("Inverse of the matrix is",Y)
