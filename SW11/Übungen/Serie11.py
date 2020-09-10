# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:31:26 2020

@author: freya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from pandas import DataFrame
from statsmodels.graphics.factorplots import interaction_plot
import statsmodels.api as sm
from statsmodels.graphics.regressionplots import abline_plot

df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW11\Übungen\Auto.csv", index_col=0)
df.head()

# Serie 11
# Aufgabe 11.1
# a)
# mpg = b0 + b1 * horsepower

# b)
y = df["mpg"]
x = df["horsepower"]
x = sm.add_constant(x)

fit = sm.OLS(y,x).fit()
fit.params

fit.summary()

# i)
# laut p-wert statistisch signifikant

# ii)
# start y = 39 steigung aber negativ = 0.158

# iii)
fit.conf_int()
#                     0          1
# const       38.525212  41.346510
# horsepower  -0.170517  -0.145172

# iv)
fit.rsquared

# c)
ax = df.plot(kind="scatter",x="horsepower", y="mpg")
abline_plot(model_results=fit, ax = ax, color="orange", linewidth=3)



# Aufgabe 11.2
# a)
df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW11\Übungen\Boston.csv", index_col=0)
df.head()
df.columns

# b)
# i)
# medv = bo + b1 * lstat

# ii)
y = df["medv"]
x = df["lstat"]
x = sm.add_constant(x)
fit = sm.OLS(y,x).fit()
fit.params

fit.summary()

# c)
# in b)

# d)
fit.conf_int()

# e)
ax = df.plot(kind="scatter",x="lstat", y="medv")
abline_plot(model_results=fit, ax = ax, color="orange", linewidth=3)

# f)
fit.rsquared

























    


