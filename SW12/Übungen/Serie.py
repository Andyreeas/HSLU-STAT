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


df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW11\Übungen\Boston.csv", index_col=0)
df.head()

# Serie 12
# Aufgabe 12.1
# a)
# medv = b0 + b1 * lstat + b2 * age

y = df["medv"]
x = df[""]



# b)



















