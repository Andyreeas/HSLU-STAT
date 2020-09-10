# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 16:51:05 2020

@author: freya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, expon, norm

# Serie 5
# Aufgabe 5.1
# a)
norm.cdf(x=10, loc=8.2, scale=np.sqrt(36/36))

# b)
norm.cdf(x=10, loc=8.2, scale=np.sqrt(36/36)) - norm.cdf(x=5, loc=8.2, scale=np.sqrt(36/36))

# c)
1 - norm.cdf(x=20, loc=8.2, scale=1)

# d)
# Normalverteilung --> Glockenkruve beinhaltet keine Extreme

# e)
# Nein

# Aufgabe 5.2
# a)
norm.cdf(x=80, loc=75, scale=np.sqrt(4.5))

# Aufgabe 5.3
# a)
norm.cdf(x=104, loc=100, scale=np.sqrt(400/16))

# b)
norm.cdf(x=104, loc=100, scale=np.sqrt(400/16)) - norm.cdf(x=98, loc=100, scale=np.sqrt(400/16))

# Aufgabe 5.4
# a)
norm.cdf(x=3.1, loc=2.2, scale=np.sqrt(0.09/100))

# Aufgabe 5.5
# a)
norm.cdf(x=82, loc=77, scale=np.sqrt(225/25)) - norm.cdf(x=72, loc=77, scale=np.sqrt(225/25))

# b)
norm.cdf(x=82, loc=77, scale=np.sqrt(225/64)) - norm.cdf(x=72, loc=77, scale=np.sqrt(225/64))

# Aufgabe 5.6
# a)
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
n = 5
m = 500
ran = np.array(norm.rvs(size=n*m))
sim = ran.reshape((n,m))
plt.plot(sim)
plt.show()

# b)
plt.hist(sim.T, bins=20, density=True, edgecolor="black",
facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x)
plt.plot(x,y)
plt.title("Histogramm sim")
plt.show()
sim_mean = sim.mean(axis=0)
plt.hist(sim_mean, density=True, edgecolor="black",
facecolor="white")
x = np.linspace(-4, 4, num=100)
y = norm.pdf(x, loc=0, scale=1/np.sqrt(n))
plt.plot(x,y)
plt.title("Histogramm sim_mean")
plt.show()

# c)

# Aufgabe 5.7
# a)
norm.cdf(x=95, loc=100, scale=np.sqrt(2))

# b)


# Aufgabe 5.8
# a)
# Sn E=n*u --> 50 * 1
# Sn O=sqrt(50) * 2
# Xn E=u
# Xn O=2/sqrt(50)

# b)
norm.cdf(x=2, loc=1, scale=2) - norm.cdf(x=0, loc=1, scale=2)

# c)
norm.cdf(x=51, loc=50, scale=np.sqrt(200)) - norm.cdf(x=49, loc=50, scale=np.sqrt(200))

# d)
norm.cdf(x=2, loc=1, scale=np.sqrt(4/50)) - norm.cdf(x=0, loc=1, scale=np.sqrt(4/50))

