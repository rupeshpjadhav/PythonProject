x = int(input("Enter number to find factorial: ")) 
# 5! = 5 * 4* 3* 2 *1
f=1

for i in range(1,x+1): #forward logic
    f = f*i
print(f)   

fa=1 
for i in range(x,1,-1): #reverse logic
    fa = fa*i
print(fa)   
 
#Approach 2 using recursion 

def fact(x):
    if x == 0 or x ==1: 
        return 1
    return (x * fact(x-1))
 
print (fact(5)) 

''' 
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1
= 120 
'''