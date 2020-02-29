from numpy import genfromtxt
from sklearn import linear_model

dataPath = r"Delivery.csv"
deliveryData = genfromtxt(dataPath,delimiter=',')

print "data"
print deliveryData

x= deliveryData[:,:-1]
y = deliveryData[:,-1]

print x
print y

lr = linear_model.LinearRegression()
lr.fit(x, y)

print lr

print("coefficients:")
print lr.coef_

print("intercept:")
print lr.intercept_

xPredict = [102,6]
yPredict = lr.predict(xPredict)
print("predict:")
print yPredict
