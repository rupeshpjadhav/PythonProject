x=20
y=5

for i in range(y+1): #solid rectangle
        print ("*" * x)

print ("\n          ")

for i in range(1,y+1): #hollow rectangle
        if i == 1:
            print ("*" * x)
        elif (i>1 and i<y):
            print("*" + " " * (x-2) + "*")
        else: 
            print ("*" * x)    

print ("\n          ")      

l=10
for i in range(l): #square
    print ("*" * l)