# -*- coding: utf-8 -*-
'''
###############################################################################
#          basics
###############################################################################

# libraries included in Anaconda

- NumPy: library used to handle large arrays
- SciPy: library containing many useful scientific functions
         - solution of linear or nonlinear equations
         - optimisation
         - numberical integration
- Matplotlib: library used to plot
- Pandas: library to analyze effectively and fast large datasets, time series
- Sympy: symbolic computation

'''



'''
###############################################################################
#    numpy
###############################################################################

Numpy provides a new data type: ndarray(n-dimensional array).
    - arrays can only store objects of the same type(only floats or only ints)

'''


import numpy as np
#%%

# create ndarray
print(np.array([1,2,3]))

# create evenly spaced arrays
print(np.arange(5))

a = np.linspace(0, 0.25, 5) # linspace(start, stop, total numbers)
print(a)

# create matrix
a = np.array([1,2,3], [4,5,6])
print(a)
print(a.shape) # number of rows and columns
print(a.ndim) # number of dimentions
print(a.size) # total number of elements
#%%

# change shape
a = np.arange(0, 30, 1) # 1 dimention
print(a)

b = a.reshape((5, 6))
print(b)
#%%

# filling the array with random numbers

# random numbers uniformly distributed between 0 and 1
np.random.rand(2, 5) # (2, 5) indicates the size of this array

# normal distribution with variance 1 and mean 0
np.random.randn(2, 5) # (2, 5) indicates the size

### other distributions are also available.
#%%

# saving arrays to files

a = np.linspace(0, 1, 12)
a.shape = (3, 4)
np.savetxt('filename.txt', a)

np.save('file', a) # save a in a binary file in NumPy (.npy) format
np.load('file.npy')
#%%

# read text file into arrays
table = np.loadtxt('filename.txt')
table
#%%


'''
###############################################################################
        SciPy
###############################################################################

> scipy.integrate: integration and ordinary differential equations
> scipy.linalg: linear algebra
> scipy.ndimage: image processing
> scipy.optimize: optimisation and root finding
> scipy.special: special functions
> scipy.stats: statistical funcitons

'''

# Linear algebra

from scipy import linalg
import numpy as np

A = np.random.randn(5, 5)
b = np.random.randn(5)

x = linalg.solve(A, b) # A x = b
print(x)

eigen = linalg.eig(A) # eigens
print(eigen)

det = linalg.det(A) # determinant
print(det)
#%%


# numerical integration

# integrate.quad is a function for adaptive numerical quadrature of one-dimensional
# integrals.
import numpy as np
from scipy import integrate

def fun(x):
    return np.log(x)

value, error = integrate.quad(fun, 0, 1)
print(value)
print(error)
#%%

# statistics in scipy

from scipy import stats

y = stats.norm.cdf(1.2) # cummulative density function of a stardard normal distribution
#%%

#  optimisation: data fitting

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def func(x, a, b, c):
    return a * np.exp(-b * x) + c
    
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
ydata = y + 0.2 * np.random.normal(size = len(xdata))

popt, pcov = curve_fit(func, xdata, ydata)

plt.plot(xdata, ydata, 'b*')
plt.plot(xdata, func(xdata, popt[0], popt[2], popt[2]), 'r-')
plt.title('$f(x) = ae^{-bx}+ c$ curve fitting' )
#%%


# optimisation: root searching
import numpy as np
from scipy import optimize

def fun(x):
    return np.exp(np.exp(x)) - x**2

# find zero of fun with initial point 0 by Newton-Raphson
value1 = optimize.newton(fun, 0)
print(value1)

# find zero between (-5, 5) by bisection
value2 = optimize.bisect(fun, -5, 5)
print(value2)
#%%


'''
###############################################################################
    Matplotlib
###############################################################################
    

'''

# simplest plot

# plot a function
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 201)

plt.figure(figsize = (3, 3))
plt.plot(x, x**0.3, 'r--')
plt.plot(x, x-1, 'k-')
plt.plot(x, np.zeros_like(x), 'k-')
#%%

# multiple plotting, legends, labels and title
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 201)
plt.figure(figsize = (4, 4))

for n in range(2, 5):
    y = x ** (1/n)
    plt.plot(x, y, label = 'x^(1/' + str(n) + ')')
plt.legend(loc = 'best')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-2, 10)
plt.title('multiple plot', fontsize = 18)
#%%

# subplots
import numpy as np
import matplotlib.pyplot as plt

def pffcall(s, k):
    return np.maximum(s -k, 0.0)

def pffput(s, k):
    return np.maximum(k -s, 0.0)

s = np.linspace(50, 151, 100)
fig = plt.figure(figsize = (12, 6))

sub1 = fig.add_subplot(121) # col, row, num
sub1.set_title('call', fontsize = 18)
plt.plot(s, pffcall(s, 100), 'r-', lw = 4)
plt.plot(s, np.zeros_like(s), 'black', lw = 1)
sub1.grid(True)
sub1.set_xlim([60, 120])
sub1.set_ylim([-10, 40])

sub2 = fig.add_subplot(122)
sub2.set_title('put', fontsize = 18)
plt.plot(s, pffput(s, 100), 'r-', lw = 4)
plt.plot(s, np.zeros_like(s), 'black', lw = 1)
sub2.grid(False)
sub2.set_xlim([60, 120])
sub2.set_ylim([-10, 40])
#%%

# adding texts to plots

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def call(s, k = 100, t = 0.5, vol = 0.6, r = 0.05):
    d1 = (np.log(s/k) +(r+0.5*vol**2)*t)/np.sqrt(t)/vol
    d2 = (np.log(s/k)+(r-0.5*vol**2)*t)/np.sqrt(t)/vol
    return s*norm.cdf(d1)-k*np.exp(-r*t)*norm.cdf(d2)

def delta(s, k = 100, t = 0.5, vol = 0.6, r = 0.05):
    d1 = (np.log(s/k)+(r + 0.5*vol**2)*t)/np.sqrt(t)/vol
    return norm.cdf(d1)

s = np.linspace(40, 161, 100)
fig = plt.figure(figsize = (7, 6))
ax = fig.add_subplot(111)
plt.plot(s, (call(s) - call(100)), 'r', lw = 1)
plt.plot(100, 0, 'ro', lw = 1)
plt.plot(s, np.zeros_like(s), 'black', lw = 1)
plt.plot(s, call(s) - delta(100)*s-(call(100)-delta(100)*100), 'y', lw = 1)


ax.annotate('$\delta$ hedge', xy=(100, 0), xytext = (100, -1), \
arrowprops = dict(headwidth = 3, width = 0.5, facecolor = 'black', \
shrink = 0.05))
# name, the location being annotated (xy), 
# the location of text (xytext), 
# information of arrows:
#     width: the width of the arrow in points
#     frac: the fraction of the arrow length occupied by the head
#     headwidth: the width of the base of the arrow head in points
#     shrink: move the tip and base some percent away from the annotated
#             point and text
#     **kwargs: any key for matplotlib.patches.Polygon, e.g., facecolor



ax.annotate('original call', xy = (120, call(120)-call(100)), \
xytext = (130, call(120)-call(100)), \
arrowprops = dict(headwidth = 10, \
width = 3, facecolor = 'r', shrink = 0.05))

plt.grid(True)
plt.xlim(40, 160)
plt.xlabel('stock price', fontsize = 18)
plt.ylabel('profits', fontsize = 18)
#%%


#    3D plot of a function with 2 variables

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

x, y = np.mgrid[-5 : 5: 100j, -5 : 5: 100j]
z = x**2 + y**2
fig = plt.figure(figsize = (8, 6))
ax = plt.axes(projection = '3d')
surf = ax.plot_surface(x, y, z, rstride = 1, cmap = cm.coolwarm, \
cstride = 1, linewidth = 0)
fig.colorbar(surf, shrink = 0.5, aspect = 5)
plt.title('3D plto of $z = x^2 + y^2$')
#%%

'''
###############################################################################
         Sympy
###############################################################################

Symbolic computation can be useful for calculating explicit solutions to equations,
integrations and so on.

'''

# declare a symbol variable

import sympy as sy

# declare x and y are variables
x = sy.Symbol('x')
y = sy.Symbol('y')
a, b = sy.symbols('a, b')

# create a new symbol (not function)
f = x**2 + y**2 - 2*x*y +5
print(f)

# auto simplify
g = x**2 + 2 - 2*x + x**2 - 1
print(g)
#%%

# use of symbol 1: solve equations

import sympy as sy
x = sy.Symbol('x')
y = sy.Symbol('y')

# solve x^2 - 1 = 0
print(sy.solve(x**2 - 1))

# solve x^3 + 0.5x^2 - = 0
print(sy.solve(x**3 + 0.5*x**2 - 1))

# express x in terms of y
# x^3 + y^2 = 0
print(sy.solve(x**3 + y**2))
#%%

# use of symbole 2: integration

import sympy as sy
x = sy.Symbol('x')
y = sy.Symbol('y')
a , b = sy.symbols('a, b')

'''
single variable
'''
f = sy.sin(x)+sy.exp(x)
print(sy.integrate(f, (x, a, b)))
print(sy.integrate(f, (x, 1, 2)))
print(sy.integrate(f, (x, 1.0, 2.0)))
# integral object, lower limit, upper limit

'''
multi variables
'''

g = sy.exp(x) + x * sy.sin(y)

print(sy.integrate(g, (y, a, b)))
print(sy.integrate(g, (x, a, b)))
#%%

# use of symbol 3: differentiation

import sympy as sy
x = sy.Symbol('x')
y = sy.Symbol('y')

f = sy.cos(x) + x**x
print(sy.diff(f, x))

g = sy.cos(y) * x + sy.log(y)
print(sy.diff(g, y))
# function, differentiation object
#%%

