# list 10
max1 = [
         [1, 3],
         [2, 4]
       ]
max2 = [
        [5, 2],
        [1, 0]
       ]
max3 = []

for outer in range(len(max1)):
    max_inner = []
    for inner in range(len(max1[outer])):
        max_inner.append(max1[outer][inner] + max2[outer][inner])

    max3.append(max_inner)

for inner_list in max3:
    for inner_num in inner_list:
        print(inner_num, end=" ")

    print("")
# list 9
max3 = [[0, 0], [0, 0]]

max3[0][0] = max1[0][0] + max2[0][0]
max3[0][1] = max1[0][1] + max2[0][1]
max3[1][0] = max1[1][0] + max2[1][0]
max3[1][1] = max1[1][1] + max2[1][1]

print(max3)
