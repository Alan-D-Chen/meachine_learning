# -*- coding: utf-8 -*-
# @Time    : 2020/02/28 下午 10:47
# @Author  : Alan D. Chen
# @FileName: simple_linaer_regaression.py
# @Software: PyCharm

import numpy as np

def fitSLR (x , y) :
    n = len(x)
    dim = 0
    mune = 0
    for i in range(0,len(x)):
        mune += (x[i] - np.mean(x))*(y[i] - np.mean(y))
        dim += (x[i] - np.mean(x))**2
    print("numerator:" , mune , "\n" , "dinominator:",dim)
    b1 = mune/float(dim)
    b0 = np.mean(y)/float(np.mean(x))

    return(b0,b1)

def predict(x , b0 ,b1):
    return(b0 + x*b1)

x = [1,3,2,1,3]
y = [14,24,18,17,27]

b0,b1 = fitSLR(x,y)
print("intercept:",b0,"\n","slope",b1)

print("please input x_test:")
x_t = float(input())
y_t = predict(x_t,b0,b1)

print("x_t:",x_t,"\n","y_t:",y_t)