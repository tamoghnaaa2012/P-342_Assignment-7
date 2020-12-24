#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import random


def euler( x0, y, h,func, x,file ): 
    temp = 0
    file.write("{:<15}{:<15}\n".format(x0, y))
  
    # Iterating till the point at which we 
    # need approximation 
    while x0 < x: 
        temp = y 
        y = y + h * func(x0, y) 
        x0 = x0 + h 
        
        file.write("{:<15.6}{:<15.10}\n".format(x0, y))
        
        #print(  "%.6f"% x0,"      ","%.6f"% y)
    return 0






def rk4(x0, y0,z0, h,func1,func2,x,file):
    file.write("{:<15}{:<15}\n".format(x0, y0))
    while x0<x:
        k1y = h * func1(x0, y0, z0)
        k1z = h * func2(x0, y0, z0)
        
        k2y = h * func1((x0 + h/2), (y0 + k1y/2), (z0 + k1z/2))
        k2z = h * func2((x0 + h/2), (y0 + k1y/2), (z0 + k1z/2))
        
        k3y = h * func1((x0 + h/2), (y0 + k2y/2), (z0 + k2z/2))
        k3z = h * func2((x0 + h/2), (y0 + k2y/2), (z0 + k2z/2))
        
        k4y = h * func1((x0 + h), (y0 + k3y), (z0 + k3z))
        k4z = h * func2((x0 + h), (y0 + k3y), (z0 + k3z))
        
        y = y0 + (1/6 * (k1y + (2 * k2y) + (2 * k3y) + k4y))
        z0 = z0 + (1/6 * (k1z + (2 * k2z) + (2 * k3z) + k4z))
        x0 = x0 + h
        y0 = y
        
        file.write("{:<15.6}{:<15.10}\n".format(x0, y0))
        
        #print(  "%.6f"% x0,"      ","%.6f"% y)
        #print( x0, "                ",y)
    return(y0)    
   
    
    
    

    
    
    
def shoting_method(x0, y0, zh0, zl0, xn, yn, h, func1, func2, file1, file2):
    yh = rk4(x0, y0, zh0, h, func1, func2, xn, file1)
    yl = rk4(x0, y0, zl0, h, func1, func2, xn, file2)
    print("For boundary condition, Yn = ", yn)
    if yh > yn and yl < yn:
        while abs(yh - yn) > 0.001 or abs(yl - yn) > 0.001:
            if abs(yh - yn) > abs(yn - yl):
                zh0 = zl0 + (((zh0 - zl0)/(yh - yl)) * (yn - yl))

            elif abs(yh - yn) < abs(yn - yl):
                zl0 = zl0 + (((zh0 - zl0) / (yh - yl)) * (yn - yl))
            yh = rk4(x0, y0, zh0, h, func1, func2, xn, file1)
            yl = rk4(x0, y0, zl0, h, func1, func2, xn, file2)
    elif yh < yn and yl < yn:
        return print("please change your 'zh' ")

    elif yh > yn and yl > yn:
        return print("please change your 'zl' ")

    elif yh < yn and yl > yn:
        return print("please change your 'zl' and 'zh'")
    print("After Langarangian interpolation, The value of Z =", zh0)
    print("And for Z =", zh0, ", The calculated value of Yn =", yh)
    
    
    

    
    
    

