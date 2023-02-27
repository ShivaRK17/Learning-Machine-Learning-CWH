# Typesof Gradient Descent - Mini Batch , Stochastic G.D etc

# COnsider to a model you are giving features and labels 
# You can easily train it and compute the loss (consider SSE) by sigma(y-yi)2
# What if there are one million datasets given?
# Just computing the loss or SSE takes much time then how will you process it?
# Here, Batch size is 1M

# Divide the Batch into 100s and now computing loss
# Doing this with seperate sets and updating parameters doesn't actually change much!
# This is called Mini Batch G.D

# If we take 1 (feature, label )(is Batch size) at a time and process, it is called Stochastic G.D 

# Algorithm | Batch Size
# ~~~~~~~~~~~~~~~~~~~~~~~
# Stochastic|    1
# General GD|   1M
# Mini Batch|   n -> as choosen by data scientists( we make n size packets out of those million and test each)