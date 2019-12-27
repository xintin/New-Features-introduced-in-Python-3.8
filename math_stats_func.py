'''
We will see a few new functions included in math library
'''

import math

print(math.prod((2,3,4,5)))
#120

a=list(range(2,10))
#[2, 3, 4, 5, 6, 7, 8, 9]

print(math.prod(a[2:4]))
#20

'''
math.isqrt()
Can be used to get the integer part of the square root of a whole number.
isqrt() truncates the answer down to the next integer, in this case 3.
'''

num = 15
print(math.sqrt(num))
#3.872983346207417
print(math.isqrt(num))
#3


'''
One can find the distance between two points with math.dist(), and the 
length of a vector with math.hypot(). 
math.dist() will work for n dimensions provided both have the same number
of dimensions. 
'''

point_1 = (16, 25, 20, 15)
point_2 = (8, 15, 14, 13)

print(math.dist(point_1, point_2))
#14.282856857085699

print(math.hypot(*point_1))
#38.80721582386451

'''
fmean - calculates the mean of float numbers.
geometric_mean - calculates the geometric mean of float numbers.
multimode - finds the most frequently occurring values in a sequence.
quantiles - calculates cut points for dividing data into n continuous 
            intervals with equal probability.
NormalDist - makes it more convenient to work with the Gaussian normal 
             distribution.
'''

import statistics

data = [9, 3, 2, 1, 1, 2, 7, 9]
print(statistics.fmean(data))
#4.25

print(statistics.geometric_mean(data))
#3.013668912157617

print(statistics.multimode(data))
#[9, 2, 1]

print(statistics.quantiles(data, n=4))
#[1.25, 2.5, 8.5]




'''
In the below example we will compare the execution time of mean and fmean. 
To get reliable results, let timeit execute each function 100 times, and 
collect 30 such time samples for each function. Based on these samples, 
create two NormalDist objects.
'''

import random
from timeit import timeit

# Create 10,000 random numbers
data = [random.random() for _ in range(10_000)]

# Measure the time it takes to run mean() and fmean()
t_mean = [timeit("statistics.mean(data)", number=100, globals=globals()) for _ in range(30)]
t_fmean = [timeit("statistics.fmean(data)", number=100, globals=globals()) for _ in range(30)]

# Create NormalDist objects based on the sampled timings
n_mean = statistics.NormalDist.from_samples(t_mean)
n_fmean = statistics.NormalDist.from_samples(t_fmean)

# Look at sample mean and standard deviation
print(n_mean.mean, n_mean.stdev)
#0.720114816700152 0.12892275121270447

print(n_fmean.mean, n_fmean.stdev)
#0.01970195770045393 0.006431530369930693

# Calculate the lower 1 percentile of mean
print(n_mean.quantiles(n=100)[0])
#0.42019564850098073





#Additional References

#https://docs.python.org/3/whatsnew/3.8.html#statistics
#https://docs.python.org/3.8/library/statistics.html#normaldist-objects
#https://www.statsmodels.org/stable/index.html
#https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html