# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:50:06 2020

@author: freya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, expon, norm

# Serie 4
# Aufgabe 4.1
# a)
1 - norm.cdf(x=1.85, loc=1.8, scale=0.074)

norm.cdf(x=1.8, loc=1.80, scale=0.074) - norm.cdf(x=1.7, loc=1.80, scale=0.074)

# b)
norm.ppf(q=[.25,.75], loc=1.80, scale=0.074)

# c)
norm.ppf(q=.95, loc=1.80, scale=0.074)

# Aufgabe 4.2
# a)
# A = 1/8
# X - Exp(A), A > 0
# E(x) = 1/(1/8) = 8
# b)
1 - expon.cdf(x=10, loc=0, scale=8)

# Aufgabe 4.3
# a)
# Skizze Lösungen

# b)
norm.cdf(x=40, loc=32, scale=6)

norm.cdf(x=(40-32)/6)

# c)
norm.cdf(x=27, loc=32, scale=6)

# d)
norm.ppf(q=.975, loc=32, scale=6)

# e)
norm.ppf(q=.1, loc=32, scale=6)

# f)
norm.cdf(x=38, loc=32, scale=6) - norm.cdf(x=26, loc=32, scale=6)

# Aufgabe 4.4
# a)
1 - norm.cdf(x=0.9, loc=0, scale=0.45)

# b)
norm.ppf(q=[.005,.995], loc=0, scale=0.45)

# c)
norm.cdf(x=0.9, loc=1.8, scale=0.45)

# Aufgabe 4.5
# a)
# TODO

# Aufgabe 4.6
# a)
# Im Onenote

# b)
# TODO




















