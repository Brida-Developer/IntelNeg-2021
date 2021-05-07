from matplotlib import pyplot

def f(x):
    return 4*x-7

x = range(-19, 29)
pyplot.plot(x, [f(i) for i in x])
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

pyplot.xlim(-11, 11)
pyplot.ylim(-11, 11)

pyplot.show()