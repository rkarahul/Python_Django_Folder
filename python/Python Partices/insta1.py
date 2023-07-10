n=5
for i in range(n):
    for j in range(1,n-1):
        print(" ",end=" ")
        for k in range (0,i+1):
            print("*",end=" ")
        print()