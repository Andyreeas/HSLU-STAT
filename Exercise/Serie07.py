# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 16:27:57 2020

@author: freya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, expon, norm, ttest_1samp, t

# Serie 07
# Aufgabe 7.2
# a)
norm.interval(alpha=[.99], loc=31, scale=6/np.sqrt(10))

# b)
n = 40
a = norm.interval(alpha=[.99], loc=31, scale=6/np.sqrt(n))
a[1] - a[0]


n = 0
while True:
    n = n + 1
    p_n = norm.ppf(q=[0.005, 0.995], loc=31, scale=6/np.sqrt(n))
    if (p_n[1] - p_n[0]) < 1:
        break
print(n)

# c)
a = t.interval(alpha=.99, df=9, loc=31, scale=6/np.sqrt(10))
a[1] - a[0]

# Aufgabe 7.3
# a)
t.interval(alpha=.95, df=8, loc=-403, scale=3.127/np.sqrt(9))

# b)
# -400 liegt nicht im vertrauensintervall
# Beobachtung und Hypothese passen nicht zusammen

# Aufgabe 7.4
# a)
# H0 = 500
# Ha > 500
# 

# b)
# Verwerfungsbereich
schrauben = pd.Series([520, 512, 499, 524, 505])
schrauben.std()
t.ppf(q=0.95, df=4, loc=500, scale=schrauben.std()/np.sqrt(5))


# Teststatistik
print(schrauben.mean())

# c)
t.interval(alpha=.95, df=4, loc=512, scale=schrauben.std()/np.sqrt(5))
t.ppf(q=[.025,.975], df=4, loc=512, scale=schrauben.std()/np.sqrt(5))

# d)
norm.ppf(q=[.025,.975], loc=512, scale=schrauben.std()/np.sqrt(5))

# e)
# i == True
# ii == True
# iii == True
# iv == True
# v == True
