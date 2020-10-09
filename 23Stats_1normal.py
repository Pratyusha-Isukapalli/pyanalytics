#normal distribution
#The normal distribution is a form presenting data by arranging the probability distribution of each value in the data.
#Most values remain around the mean value making the arrangement symmetric.
#We use various functions in numpy library to mathematically calculate the values for a normal distribution. 
#Histograms are created over which we plot the probability distribution curve.

import matplotlib.pyplot as plt
import numpy as np



mu, sigma = 65, 10

s = np.random.normal(mu, sigma, 100)
s

plt.figure(1,figsize=(5,5),dpi=72)
count, bins, ignored = plt.hist(s, 10)
bins
count
ignored

plt.show();
