size=int(input("Matrix Multiplication \nEnter the size of the matrices "))

def entermatrix(size):
    T=[[0 for w in range(size)] for t in range(size)]
    for i in range(size):
        for j in range(size):
            T[i][j]=int(input("Enter "+str(i)+" row and "+str(j)+" column "))
    return T

def multiply(X,Y):
    result=[[0 for w in range(size)] for t in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += X[i][k]*Y[k][j]
    print(result)
            

print("\nEnter 1st matrix")
X=entermatrix(size)
print("\nEnter 2nd matrix")
Y=entermatrix(size)
multiply(X,Y)