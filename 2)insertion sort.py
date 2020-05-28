def insertionsort(mylist):   #function definition
    for i in range(1,len(mylist)):  
        a=mylist[i]
        b=i-1
        while b>0 and a<mylist[b]:
            mylist[b+1]=mylist[b]
            b -= 1
        mylist[b+1]=a
        
mylist = [1,2,3,4,8,5,6]
insertionsort(mylist)
for i in range (len(mylist)):   #to print the final list
    print(mylist[i])
