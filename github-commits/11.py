# manual removal
list1 = [2, 6, 6, 8]
del list1[1];
print(list1)

# loop removal
list1 = [2, 4, 6, 6, 8]
list2 =[]
for num in list1:
    if num not in list2:
        list2.append(num)

print(list2)
        
