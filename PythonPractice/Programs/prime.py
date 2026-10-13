#To check if given number is prime or not, divisible by only 1 and itself

#Approach1
n = int(input("Enter a number: "))
l = []
if n>1:
    count=0
    for i in range(2,n+1):
        if (n%i ==0):
            count = count+1           
            l.append(i)
    if count >= 2:
        print(f"{n} is not a prime number, it is divisible by {l}") 
    else:
        print(f"{n} is a prime number")      
        
#Approach 2
m = int(input("Enter a number: "))
is_prime = True
if m>1:
    for j in range(2,m):
        if (m%j ==0): #if divisor found between 2 and n-1, then it is not prime
            is_prime = False
            break
  
        else:
            is_prime = True
    
    if is_prime:
        print(f"{m} is a prime number") 
    else:
        print(f"{m} is not a prime number")        