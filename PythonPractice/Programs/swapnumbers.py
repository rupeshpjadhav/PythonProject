a=100
b=200

print (f"Values of a and b before swapping are {a} and {b}")
#approach 1 using temp variable

temp = a
a = b
b = temp

print (f"Values of a and b after swapping are {a} and {b}")


#approach 2 using tupple unpacking

x = 20
y = 50 
print (f"Values of x and y before swapping are {x} and {y}")

x,y = y,x 
print (f"Values of x and y after swapping are {x} and {y}")

#approach 3 using no temp variable

l = 30
m = 60

print (f"Values of l and m before swapping are {l} and {m}")

l = l+m #90
m = l - m #30
l = l - m #60


print (f"Values of l and m after swapping are {l} and {m}")
