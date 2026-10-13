l = [12,14,18,20,35,11]
print(f"Original list is {l}" )
min = min(l)
max = max(l)

print (f"Min number is {min} and max number is {max}")

#to replace 12 and 11

l[0],l[-1] = l[-1], l[0]

print(f"New list is {l}" )

# to replace 14 and 35 using tuple

l = [12,14,18,20,35,11]
print(f"Original list is {l}" )
t1 = l[1], l[-2]  # tuple packing 

l[1] = t1[1]
l[-2] = t1[0]
print(f"New list is {l}" )





