#Just the basics

print("Hello, these are the basics")

a = 10
b,c = 20,30 
s = a+b+c

print("Sum of a,b,c is",s)

l = [1,2,3,4,5,6,7,8]

for i in l:
    print(i)
    
for i in l: 
    print(i,end=" ")
print()
l[1] = 12
print(l)

t = (10,11,12, "Rupesh", 15.67)
print (t)

for j in t:
    print(j)
    
d = {1:3,2:"RJ","Sr.no":123}


print (d[1])
print (d[2])
print (d["Sr.no"])

d[1] = 5
d["Sr.no"] = 456
d[4] = 78

print (d[1])
print (d[2])
print (d["Sr.no"])
print (d[4])

def add(a,b,c):
    total = a + b + c
    print ("Total is",total)
    
add(4,5,6)

for i in range(10):
    print ("i is", i)
    
li = [0,1,2,3,4,5,6,7,8,9]
print(li[:4])
print(li[1:4])
print(li[:6])
print(li[1:9:2])


s= "Rupesh Jadhav"
print (s.capitalize())
print (s.lower())
print (s.upper())
s1= "     Rupesh Jadhav.    " 
print (s1.strip())
print(s.replace("Rupesh Jadhav","Rupesh P Jadhav"))
print (s)
c= len(s)
ca= s.count("a")
print (f"Total length of {s} is {c} and count of albhabet 'a' is {ca}")



#Lets draw a pyramid
n = 10
for i in range (1,n):
    print((" " * (n-i)) + ("*" * (2*i-1)  ))
    
    
#prime number
a = 18
count = 0
f=[]
for i in range(1,a+1):
    if (a%i == 0):    
        f.append(i)
        count = count + 1
        
if count > 2:
    print (f"{a} is not a prime number, it is divisible by {f}") 
else:
    print(f"{a} is a prime number")   
    
#fibonaci - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

n = 10
a = 0
b = 1
print (a)
print (b)
for i in range(2,n+1):
        sum = a + b 
        a= b
        b = sum
        print (sum)        