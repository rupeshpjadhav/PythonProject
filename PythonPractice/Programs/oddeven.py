#Prog1

n = int(input("Enter any number: "))

if n % 2 == 0:
    print (f"{n} is an even number")
else:
    print (f"{n} is an odd number")
    
    
#Prog2

n = int(input("Enter a number to print odd/even numbers till that entered number : "))
odd=[]  
even=[] 
for i in range(1,n+1):
        if (i%2) == 0:
            even.append(i)
        else:
            odd.append(i)    
print (f"Even numbers till {n} are {even}")
print (f"Odd numbers till {n} are {odd}")

        