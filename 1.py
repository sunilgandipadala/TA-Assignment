n=int(input("Enter the no of rows: "))
for i in range(n,0,-1):
    for j in range(0,i):
        if(j==0):
            continue
        else:
            print(" ",end=" ")
    for i in range(0,n-j):
        print("*",end=" ")
    print()
print("\n\n")
charasci=64
for i in range(0,n):
    for j in range(0,i+1):
        charasci+=1
        print(chr(charasci),end=" ")
    print()
        
