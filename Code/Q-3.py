import math
from Mylibrary import *



file1 = open("Q3h_p01.dat", "w+")
file2 = open("Q3l_p01.dat", "w+")

def func2(x, y, z):
    return (z+1)

def func1(x, y, z):
    return (z)

x0 = 0
y0 = 1
zh0 = 2
zl0 = 0

xn = 1
yn = 2 * (2.71828 - 1)
h = 0.05

shoting_method(x0, y0, zh0, zl0, xn, yn, h, func1, func2, file1, file2)






"""

For boundary condition, Yn =  3.43656
After Langarangian interpolation, The value of Z = 0.9999980298267261
And for Z = 0.9999980298267261 , The calculated value of Yn = 3.43656

Process finished with exit code 0


"""

