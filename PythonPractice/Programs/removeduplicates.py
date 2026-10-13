'''
Remove duplicates while preserving order.
List = [1, 2, 2, 4, 3, 1, 2]
'''

l = [1, 2, 2, 4, 3, 1, 2]
result = []
for i in l:
    if i not in result:
        result.append(i)

print (f"Here is the corrected list: {result}")