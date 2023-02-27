#best fit line is Less Sum of Squares of error
# How do we fit a given data into this best fit then? as y = mx+b
# SSE = sum_of_all(mx+b - y')**2 => mx+b is the predicted and y' is the actual value;

# if x=[1,2,3],y=[3,2,4]
# SSE(E) = (m+b-3)**2 + (2m+b-2)**2 + (3m+b-4)**2
# diff wrt m
# dE/dm = 2(m+b-3)+2(2m+b-2)2+2(3m+b-4)3
# dE/db = 2(m+b-3)+2(2m+b-2)+2(3m+b-4)

# For max and min dE/dm and dE/db = 0
# 14m+6b=19
# 6m+3b=9

# m=1/2
# b=2
# y = x/2 + 2

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model,datasets
from sklearn.metrics import mean_squared_error

x = np.array([[1],[2],[3]])
y = np.array([[3],[2],[4]])

model = linear_model.LinearRegression()
model.fit(x, y)

Y = model.predict(x)
print("weights: ",model.coef_)
print("intercept: ",model.intercept_)
print("SSE: ",mean_squared_error(y, Y))

plt.scatter(x,y)
plt.plot(x,Y)

plt.show()

# How Multi datasets?
# We use more independent variables and more constants like w0, w1, w2 etc
# SO equation now is f() = w0 + w1x1 + w2x2 + ... 