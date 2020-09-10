# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:33:40 2020

@author: freya
"""

import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW09\Übungen\InsectSprays.csv", index_col=0)
df.head()

# Serie 09
# Aufgabe 9.1
# a)
df.groupby("spray").mean()

# b)
sns.boxplot(x="spray", y="count", data=df)
sns.stripplot(x="spray", y="count", data=df)

# c)
fit = ols("count~spray", data=df).fit()
fit.summary()
fit.f_pvalue

# d)
df_n = df.loc[df['spray'].isin(["C", "D", "E"])]
df_n.head()
df['spray'].isin(["C", "D", "E"])

sns.boxplot(x="spray", y="count", data=df_n)

sns.stripplot(x="spray", y="count", data=df_n)

fit_n = ols("count~spray", data=df_n).fit()
fit_n.f_pvalue

# Aufgabe 9.2
# a)
df = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW09\Übungen\Diet.csv")
df.head()

df["weight_loss"] = df["weight6weeks"] - df["pre.weight"]
df.head()

# b) Aufgabe 9.1 a --> mit weight.loss und Diet
df.groupby("Diet").mean()

# b) Aufgabe 9.1 b --> mit weight.loss und Diet
sns.boxplot(x="Diet", y="weight_loss", data=df)
sns.stripplot(x="Diet", y="weight_loss", data=df)

# b) Aufgabe 9.1 c --> mit weight.loss und Diet
fit = ols("weight_loss~Diet", data=df).fit()
fit.summary()
fit.f_pvalue

# Aufgabe 9.3
# a)
from pandas import DataFrame
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st

df=DataFrame({
"Behandlung": np.repeat(["A", "B", "C", "D"], [4, 6, 6, 8]),
"Koagulationszeit" : [62, 60, 63, 59, 63, 67, 71, 64, 65, 66, 68, 66, 71, 67, 68, 68, 56, 62, 60, 61, 63, 64, 63, 59]})
sns.stripplot(x="Behandlung", y="Koagulationszeit", data=df)
plt.xlabel("Behandlung")
plt.ylabel("Koagulationszeit")
plt.show()
sns.boxplot(x="Behandlung", y="Koagulationszeit", data=df)
plt.xlabel("Behandlung")
plt.ylabel("Koagulationszeit")
plt.show()

# b)
fit = ols("Koagulationszeit~Behandlung", data=df).fit()
fit.summary()
fit.f_pvalue

# Aufgabe 9.4
# a)
from pandas import DataFrame
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st

df=DataFrame({
"Typ": np.repeat(["T1", "T2", "T3", "T4"], [6, 6, 6, 6]),
"Druckfestigkeit" : [655.5, 788.3, 734.3, 721.4, 679.1, 699.4, 789.2, 772.5, 786.9, 686.1, 732.1, 774.8, 737.1, 639.0, 696.3, 671.7, 717.2, 727.1, 535.1, 628.7, 542.4, 559.0, 586.9, 520.0]})

sns.stripplot(x="Typ", y="Druckfestigkeit", data=df)
plt.xlabel("Typ")
plt.ylabel("Druckfestigkeit")
plt.show()

sns.boxplot(x="Typ", y="Druckfestigkeit", data=df)
plt.xlabel("Typ")
plt.ylabel("Druckfestigkeit")
plt.show()

# b)
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
fit = ols("Druckfestigkeit~Typ", data=df).fit()
fit.params

# c)
fit = ols("Druckfestigkeit~Typ", data=df).fit()
fit.summary()
fit.f_pvalue





























