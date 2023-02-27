# We can see spams and scams happening in daily life 
# How can we classify them as spams and remove?

# Not all scams are spams
# It can be their business too!

# Consider two factors - Urgency and Money(or talk about money)
# if content talks more about money and has like more urgency ( more urgency as like showing you have failed email to a student)
# Then they are considered as spam

# YOu plot points of non spam and spam
# What if you are given a point of between them ?
# So you create a boundry between them 
# Data ->Classifier -> Trained Classifier

# Loading required modules
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris() #Koading datasets
# print(iris.keys())
# print(iris.DESCR)
features = iris.data
labels = iris.target
# print(features[0],labels[0])
# print(len(features))

# Training the classifier
clf = KNeighborsClassifier() #after including library of KNeighbour classifier
clf.fit(features, labels)
# We want to predict if sepal length,width, petal length ,width is 1,1,1,1
pred = clf.predict([[1,1,1,1]])
print(pred) #we got 0 which means it is a Iris-Setosa





# Description printed
# :Attribute Information:
#         - sepal length in cm
#         - sepal width in cm
#         - petal length in cm
#         - petal width in cm
#         - class:
#                 - Iris-Setosa -0
#                 - Iris-Versicolour -1
#                 - Iris-Virginica -2