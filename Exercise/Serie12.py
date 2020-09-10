# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 16:04:08 2020

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
pd.set_option("display.max_columns", 100)

df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW12\Übungen\Boston.csv", index_col=0)
df.head()

# Serie 12
# Aufgabe 12.1
# a)
# medv = b0 + b1 * lstat + b2 * age

y = df["medv"]
x = df[["lstat", "age"]]
x = sm.add_constant(x)

fit = sm.OLS(y,x).fit()
fit.summary()
fit.rsquared

# b)
all_columns = "+".join(df.columns.drop("medv"))
all_columns
fit = ols("medv~" + all_columns, data=df).fit()
fit.summary()

# c)
fit.rsquared

# d)



# Aufgabe 12.2
# a)
df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW12\Übungen\Auto.csv")
df.columns

df = df.drop(["Unnamed: 0", "name"], axis=1)
df.head()

sns.pairplot(df)

# b)
print(df.corr())

# c)
all_columns = "+".join(df.columns.drop("mpg"))
all_columns
fit = ols("mpg~" + all_columns , data=df).fit()
fit.summary()

# i)
# Der p-Wert zum zugehörigen F-Wert ist praktisch 0 und somit 
# besteht ein statistisch signifikanter Zusammenhang 
# zwischen Zielvariable und den Prädiktoren.

# ii)
# alle ausser cylinders, horsepower, acceleration

# iii)
# MPG steigt mit jedem jahr
# dass Heisst genau, dass jüngere Autos sparsamer sind und 
# deshalb weiter kommen

# d)
fit = ols("mpg~weight*year" , data=df).fit()
fit.summary()













