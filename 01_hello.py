# For only two features from diabetes : data and target 
# we get best fitting line even though there can be amount of error


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error


diabetes = datasets.load_diabetes()
# print(diabetes.keys)
# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module']) 

# print(diabetes.DESCR)

diabetes_X = diabetes.data[:,np.newaxis,2]
# print(diabetes_X)
diabetes_X_train = diabetes_X[-30:]
diabetes_X_test = diabetes_X[:20]

diabetes_Y_train = diabetes.target[-30:]
diabetes_Y_test = diabetes.target[:20]

model = linear_model.LinearRegression()
model.fit(diabetes_X_train,diabetes_Y_train)

diabetes_Y_predict= model.predict(diabetes_X_test)

print("Mean squared error: ", mean_squared_error(diabetes_Y_test,diabetes_Y_predict))
print("Weights: ",model.coef_)
print("Intercept: ",model.intercept_)
# Mean squared error:  3549.707098066288
# Weights:  [1045.84131827]
# Intercept:  134.94339553367877

plt.scatter(diabetes_X_test, diabetes_Y_test)
plt.plot(diabetes_X_test,diabetes_Y_predict)
plt.show()


# res = "\n".join("{} {}".format(x, y) for x, y in zip(diabetes_Y_test, diabetes_Y_predict))
# print(res)