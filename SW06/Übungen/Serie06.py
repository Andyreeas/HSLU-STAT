# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:56:00 2020

@author: freya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, expon, norm, ttest_1samp, t


# Serie06
# Aufgabe 6.1
# a)
wein = pd.Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72])

# z-test
# Verwerfungsbereich
norm.ppf(q=.05, loc=70, scale=1.5/np.sqrt(12))
# Testentscheid
wein.mean()

# Aufgabe 6.2
# a)
wein2= pd.Series([71, 69, 67, 68, 73, 72, 71, 71, 68, 72, 69, 72]) 

o = wein2.std()
o = 1.96

t.ppf(q=0.05, df=11, loc=70, scale=1.96/np.sqrt(12))

wein2.mean()

# Aufgabe 6.3
# a)
# o = 10
# H0: u = 204.2
# Ha: u > = 204.2

# Verwerfungsbereich
norm.ppf(q=.95, loc=200, scale=10/np.sqrt(16))

# Testergebniss bekannt = 204.2 ug/l
# Verwerfungsbereich bei 204.11 also überschritten

# b)
1 - norm.cdf(x=204.11, loc=205, scale=10/np.sqrt(16))

# c)
1 - norm.cdf(x=204.11, loc=200, scale=10/np.sqrt(16))

# d)
# o = 10
# H0: 204.11
# Ha: u > 204.11

# Verwerfungsbereich
t.ppf(q=.95, df=15, loc=200, scale=10/np.sqrt(16)) 

# Testbereich 204.11 < 204.3826 also sehr knapp I.O

# e)
# 
