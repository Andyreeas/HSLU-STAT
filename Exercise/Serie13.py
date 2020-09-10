# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 15:00:58 2020

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



# Serie 13
# Aufgabe 13.1
# a)
df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW13\Übungen\Carseats.csv", index_col=0)
df.head()

# b)
fit = ols("Sales~Price+Urban+US", data=df).fit()
fit.summary()

# c)
# 

# d)
# 
# Sales = b0 + b1 * price + b2*x2i + b3*x3i + ei

# e)
# Alle ausser Urban

# f)
fit = ols("Sales~Price+US", data=df).fit()
fit.summary()

# g)
ols("Sales~Price+Urban+US", data=df).fit().rsquared
ols("Sales~Price+US", data=df).fit().rsquared

# Aufgabe 13.2
df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW13\Übungen\Auto.csv").drop(["Unnamed: 0", "name"], axis=1)
df.columns

# a)
all_columns = "+".join(df.columns.drop("mpg"))
all_columns
fit = ols("mpg~" + all_columns , data=df).fit()
fit.summary()

pd.options.display.float_format = "{:.10f}".format
predictors = set(df.columns)
predictors.remove("mpg")
selected = list(predictors)
formula = "{} ~ {}".format("mpg", "+".join(selected))
ols(formula, data=df).fit().summary()

predictors.remove("acceleration")
selected = list(predictors)
formula = "{} ~ {}".format("mpg", "+".join(selected))
ols(formula, data=df).fit().summary()

predictors.remove("cylinders")
selected = list(predictors)
formula = "{} ~ {}".format("mpg", "+".join(selected))
ols(formula, data=df).fit().pvalues


# b)
def forward_selected(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {}".format(response,
                                       "+".join(selected +
                                                  [candidate]))
            score = ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {}".format(response,"+".join(selected))
    model = ols(formula, data).fit()
    return model

model = forward_selected(df, "mpg")
print(model.model.formula)



























