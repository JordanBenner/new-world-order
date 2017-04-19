numbers = [-2, 4, -8, 9]
print(numbers)
positves = []

for num in numbers:
    if '-' not in str(num):
        positves.append(num)

print(positves)
