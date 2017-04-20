#function lesson 1
#input = input('what is your name?')
#name = ('igor')
#def hello (name):
    #print('Hello ' + name)

#hello(name)


# Function lesson 2
# from matplotlib import pyplot
#
# def f(x):
#     return x + 1
#
# xs = list(range(-3, 4))
# ys = []
# for x in xs:
#     ys.append(f(x))
#
# pyplot.plot(xs, ys)
# pyplot.show()

# function lesson 3
#from matplotlib import pyplot

#def f(x):
#    return x ** 2

#xs = list(range(-100, 100))
#ys = []

#for x in xs:
#    ys.append(f(x))

#pyplot.plot (xs, ys)
#pyplot.show()

# function lesson 4
#import matplotlib.pyplot as plot

#def f(x):
#    if x % 2 != 0:
#        return 1
#    if x % 2 == 0:
#        return - 1

#xs = list(range(-5, 5))
#ys = []

#for x in xs:
#    ys.append(f(x))

#plot.bar(xs, ys)
#plot.show()

#function lesson 5
#import matplotlib.pyplot as plot
#import math
#def f(x):
#    return math.sin(x)

#xs = list(range(-5, 5))
#ys = []

#for x in xs:
#    ys.append(f(x))

#plot.plot(xs, ys)
#plot.show()

# function lesson 6
#import matplotlib.pyplot as plot
#import math
#from numpy import arange

#def f(x):
#    return math.sin(x)

#xs = list(arange(-5, 6, 0.1))
#ys = []

#for x in xs:
#    ys.append(f(x))

#plot.plot(xs, ys)
#plot.show()

# function lesson 7
#import matplotlib.pyplot as plot
#def f(x):
#    return x * 1.8 + 32

#f = list(range(-25, 45, 2))
#x = []

#for x in xs:
#    f.append(f(x))

#plot.plot(f, c)
#plot.show()


#function lesson 8

def f(user):
    user = input('do you want to play again?'('Y', 'N'))
    return user

while True:
    user = f()
    if user == 'N'
        break
