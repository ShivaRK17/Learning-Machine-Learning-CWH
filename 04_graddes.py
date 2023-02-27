# We have multiple type of errors to measure by types like
# Mean Square , Absolute error, Sum of Squares Error

# We have to find minima
# Finding direction to find minima , we use gradient descent = 
# If we take x = 5 in y = x^2 , we know we have to move left to find minim, but for multi variable or some complex function
# We use some constant learning rate (take 0.1)
# xnew = x - (L.R)(df/dx)

# therefore newx = 5 - (0.1*(2*5)) = 4
# xnew = 4-(0.1*(2*4)) = 3.2
# This moves till minima

# My own code
# Random code to see if it goes till 0...
# I want to plot it and see
import matplotlib.pyplot as plt
xlist = []
ylist = []
i = 20
x = 5 #you can use x as negative too
while(i>0):
    x = (x-0.1*(2*x))
    print("new x is ",x," y is ",x*x)
    xlist.append(x)
    ylist.append(x*x)
    i=i-1

plt.scatter(xlist, ylist)
plt.show()