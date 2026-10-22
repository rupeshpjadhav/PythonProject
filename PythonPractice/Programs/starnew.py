n=6

for i in range(1,n+1):
    for j in range(1, i+1):
        print("*",end=" ")
    print()
print("====== STAR =======")    

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()    
    
print("====== STAR =======")   

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print ("*",end=" ")
    print()
    
print("====== STAR =======")  

for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ", end=" ")
    
    for k in range(i,0,-1):
        print("*", end=" ")
    print()

print("====== STAR =======")  

for i in range (1,n+1):
    for j in range(1,n-i+1):
        print(" ", end=" ")
    for k in range(1,2*i-1+1):
        print("*", end=" ")
    print()