#Bubble sort 

l = [12,15,34,100,45,23,67]

ln = len(l) #7

for i in range(ln): # each pass
    print("i is",i)
    for j in range(0,ln-i-1): # each index is compared with next and swapped if it greater
        print ("j is",j)
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print(l)
            