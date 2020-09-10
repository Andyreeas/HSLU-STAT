# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 18:37:30 2020

@author: freya
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW010\Übungen\Diet.csv")
df["weight_loss"] = df["weight6weeks"] - df["pre.weight"]
df.head()

# Serie 10
# Aufgabe 10.1
# a)
sns.boxplot(x="gender", y="weight_loss", data=df)
sns.stripplot(x="gender", y="weight_loss", data=df)

# b)
from statsmodels.graphics.factorplots import interaction_plot
interaction_plot(x=df["gender"], trace=df["Diet"], response=df["weight_loss"])

# c)
interaction_plot(x=df["Diet"], trace=df["gender"], response=df["weight_loss"])

# d)
fit = ols("weight_loss~gender+Diet", data=df).fit()
anova_lm(fit)

# e)
fit = ols("weight_loss~Diet*gender", data=df).fit()
anova_lm(fit)

# Aufgabe 10.2
# a)
df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW010\Übungen\mathGender.dat", sep=" ")
df.head()

sns.boxplot(x="gender", y="score", data=df)
sns.stripplot(x="gender", y="score", data=df)

sns.boxplot(x="courses", y="score", data=df)
sns.stripplot(x="courses", y="score", data=df)

from statsmodels.graphics.factorplots import interaction_plot
interaction_plot(x=df["gender"], trace=df["courses"], response=df["score"])

interaction_plot(x=df["courses"], trace=df["gender"], response=df["score"])

fit = ols("score~gender+courses", data=df).fit()
anova_lm(fit)

fit = ols("score~gender*courses", data=df).fit()
anova_lm(fit)

# Aufgabe 10.3
# a)
from pandas import DataFrame
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from statsmodels.graphics.factorplots import interaction_plot

df=DataFrame({
"Luftfeuchtigkeitsniveau" : np.tile([1, 2, 3, 4], 5),
"Marke": np.repeat([1, 2, 3, 4, 5], 4),
"Energieverbrauch" : np.array([685, 792, 838 , 875, 722, 806, 893, 953, 733, 802, 880, 
                               941, 811, 888, 952, 1005, 828, 920, 978, 1023])})

# b)
fit = ols("Energieverbrauch~Marke+Luftfeuchtigkeitsniveau", data=df).fit()
anova_lm(fit)

# c)
fit = ols("Energieverbrauch~Luftfeuchtigkeitsniveau+Marke", data=df).fit()
anova_lm(fit)

# d)
interaction_plot(x=df["Luftfeuchtigkeitsniveau"], trace=df["Marke"], response=df["Energieverbrauch"])

# Aufgabe 10.4
# a)
automob = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW010\Übungen\automob.dat", sep=" ")
df = DataFrame(automob)
sns.stripplot(x="STADT", y="KMP4L", hue="AUTO", jitter=True, data=automob)

# b)
fit = ols("KMP4L ~ C(STADT,Sum)*C(AUTO,Sum)", data=automob).fit()
anova_lm(fit)

# c)
df.reset_index(inplace=True)
interaction_plot(x=df["STADT"], trace=df["AUTO"], response=df["KMP4L"])

# d)
fit_1 = ols("KMP4L~C(AUTO,Sum)", data=df[df["STADT"]=="Portland"]).fit()
anova_lm(fit_1)
fit_2 = ols("KMP4L~C(AUTO,Sum)", data=df[df["STADT"]=="San Francisco"]).fit()
anova_lm(fit_2)
fit_3 = ols("KMP4L~C(AUTO,Sum)", data=df[df["STADT"]=="Los Angeles"]).fit()
anova_lm(fit_3)

# e)
fit = ols("KMP4L~C(STADT,Sum)*C(AUTO,Sum)", data=df[df["STADT"]!="San Francisco"]).fit()
anova_lm(fit)

# Aufgabe 10.5
# a)
stream = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW010\Übungen\stream.dat", sep=" ")
df = DataFrame(stream)

sns.stripplot(x="ZNGROUP", y="DIVERSITY", hue="ZINC", jitter=True, data=df)
sns.boxplot(x="ZNGROUP", y="DIVERSITY", data=df)

# b)
fit = ols("DIVERSITY~ZNGROUP", data=df).fit()
anova_lm(fit)

# c)
fit = ols("DIVERSITY~C(ZNGROUP, Sum)", data=stream).fit()
fit.summary()

# d)
fit = ols("DIVERSITY~ZNGROUP+STREAM", data=df).fit()
anova_lm(fit)
































