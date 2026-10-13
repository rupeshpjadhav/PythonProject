#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
n = int(input("Enter number to get the fibonacci series: "))
f = []
a,b = 0,1

for _ in range (n):
    f.append(a) 
    a,b = b,(b+a)
                
print(f"Fibonacci series is {f}")

#Approach 2 using recursion 

def fib (n): 
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fib(n-1) + fib (n-2) 

for i in range (n):
    print(fib(i))