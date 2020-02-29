from numpy import genfromtxt
from sklearn import linear_model

datapath=r"Delivery_Dummy.csv"
data = genfromtxt(datapath,delimiter=",")

x = data[1:,:-1]
y = data[1:,-1]
print x
print y

mlr = linear_model.LinearRegression()

mlr.fit(x, y)

print mlr
print "coef:"
print mlr.coef_
print "intercept"
print mlr.intercept_

xPredict =  [90,2,0,0,1]
yPredict = mlr.predict(xPredict)

print "predict:"
print yPredict