#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:28:37 2020

@author: krishanbhadana
"""
def entermatrix(size):
    T=[[0 for w in range(size)] for t in range(size)]
    for i in range(size):
        for j in range(size):
            T[i][j]=int(input("Enter "+str(i)+" row and "+str(j)+" column "))
    return T

def transpose(T):
    Z=[[0 for w in range(3)] for t in range(3)]
    for i in range(3):
        for j in range(3):
            Z[j][i]=T[i][j]
    print("adjugate amtrix is"+str(Z))
    return (Z)
    
def caladjugate(T): 
    T[0][0]=(X[1][1]*X[2][2])-(X[2][1]*X[1][2])
    T[0][1]=(X[2][2]*X[1][0])-(X[2][0]*X[1][2])
    T[0][2]=(X[2][1]*X[1][0])-(X[2][0]*X[1][1])
    T[1][0]=(X[2][2]*X[0][1])-(X[2][1]*X[0][2])
    T[1][1]=(X[2][2]*X[0][0])-(X[2][0]*X[0][2])
    T[1][2]=(X[2][1]*X[0][0])-(X[2][0]*X[0][1])
    T[2][0]=(X[1][2]*X[0][1])-(X[1][1]*X[0][2])
    T[2][1]=(X[1][2]*X[0][0])-(X[1][0]*X[0][2])
    T[2][2]=(X[1][1]*X[0][0])-(X[1][0]*X[0][1])
    return (transpose(T))

def caldeterminant(X):
    det=(X[0][0]*(X[1][1]*X[2][2]-X[2][1]*X[1][2])-X[0][1]*(X[2][2]*X[1][0]-X[2][0]*X[1][2])+X[0][2]*(X[2][1]*X[1][0]-X[2][0]*X[1][1]))
    print("Determinant is"+str(det))
    return (det)

def multiply(X,Y):
    result=[[0 for w in range(3)] for t in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += X[i][k]*Y[k][j]
    print(result)

def inverse(X):
    determinant=caldeterminant(X)
    inverse=caladjugate(X)
    for i in range(3):
        for j in range(3):
            inverse[i][j]=inverse[i][j]/determinant
    print("Inverse of the matrix is:",inverse)
print("\nEnter a 3X3 matrix")
X=entermatrix(3)
inverse(X)
print("To verify the result lets multiply the matrix with its inverse , to check if identity matrix comes")
multiply(X,inverse)