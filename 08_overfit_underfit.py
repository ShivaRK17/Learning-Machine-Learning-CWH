# Overfitting and underfitting
# Example a tailer can make your clothes fit in one position of you where you raise your hands,head,etc
# That is Error is made almost 0 at that position
# Linear Regression we did made errors like SSE which is still an error
# To avoid it what if we connect all points(interpolation but straight lines simultaneously)
# That creates problem when it goes out of datasets
# This is called Overfitting -> Low training error & High Test error
# 
# Underfitting -> High training error and less test error
#   if training is only /has more error , then test will be for sure more error -> so not discussed
# 
# We have 2 methods to solve over/underfitting
# !. resampling
# 2.Holding a validation data set
# 

# Resampling involves making some of given data as train data and other as test(if 1000 data sets are there , 700 for train , 300 for test)
# We can do it for k times

# Holding a validation data set involves taking some of data sets outside, we check with these dataset if there's any overfitting
# like it got used to given training data -- we dont give test data yet because we want to check it if it's perfect with train data only
