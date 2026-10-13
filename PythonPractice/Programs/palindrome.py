l = [1,2,3,2,4]
lr= l.copy()
lr.reverse()

print (l)
print(lr)

if l == lr:
    print ("The list is palindrome")
else:
    print("The list is not palindrome")
    
    
#String approach 1

s = "abcdcba"
n= s[::-1]

print (s)
print(n)
if s.__eq__(n):
    print(f"String {s} is palindrome")
else:
    print(f"String {s} is not palindrome")
    
    
#string approach 2 using loop

st = "abcdefedcba"
st2= ""

for i in range(len(st)-1,-1,-1):
    st2 = st2 + st[i]

print (st)
print(st2)
if st.__eq__(st2):
    print(f"String {st} is palindrome")
else:
    print(f"String {st} is not palindrome")