# loops 1-10
for number in range(1, 11):
    print(number)

    #loops n to m
start = int(input('what is the number to start with?'))
end = int(input('what is the number to end with?'))
number = 0
for number in range(start -1, end):
    number += 1
    print(number)

    # odd numbers
    number =0
    for number in range(1, 10):
        if number % 2 !=0:
            print(number)

# print square
i = 0
while i < 5:
    print('*'* 5)
    i += 1

#print square 2
num = int(input('how big is the square?'))
i = 0
while i < num:
    print('*' * num)
    i += 1

#print a box
width = int(input('width?'))
height = int(input('height?'))
w = 5
h = 6
print('*' * w)
for i in range(h - 2):
    print('*', end="")
    for j in range(w - 2):
        print(' ', end="")

    print('*')

print('*' * w)

'''# Print triangle
t =1
t2 = 3
m = 5
b = 7
print('*' * t)
print('*' * t2)
print('*' * m)
print('*' * b)
'''

def pyramid(rows = 4):
    for i in range(rows):
        print(' '*(rows-i-1)+ '*'*(2*i+1))
