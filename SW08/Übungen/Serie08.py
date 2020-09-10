# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:55:45 2020

@author: freya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

# Serie 08
# Aufgabe 8.1
# a)
n = 500
x = st.norm.rvs(size=n)
st.probplot(x,plot=plt)

# b)
x = st.t.rvs(size=20, df=20)
st.probplot(x,plot=plt)

x = st.t.rvs(size=100, df=20)
st.probplot(x,plot=plt)

x = st.t.rvs(size=20, df=7)
st.probplot(x,plot=plt)

x = st.t.rvs(size=100, df=7)
st.probplot(x,plot=plt)

x = st.t.rvs(size=20, df=3)
st.probplot(x,plot=plt)

x = st.t.rvs(size=100, df=3)
st.probplot(x,plot=plt)

# c)
plt.subplot(2,2,1)
x = st.chi2.rvs(size=20, df=20)
st.probplot(x,plot=plt)
plt.title("n=20, df=20")

plt.subplot(2,2,2)
x = st.chi2.rvs(size=100, df=20)
st.probplot(x,plot=plt)
plt.title("n=100, df=20")

plt.subplot(2,2,3)
x = st.chi2.rvs(size=20, df=1)
st.probplot(x,plot=plt)
plt.title("$n=20, df=1")

plt.subplot(2,2,4)
x = st.chi2.rvs(size=100, df=1)
st.probplot(x,plot=plt)
plt.title("n=100, df=1")

plt.tight_layout()
plt.show()

# Aufgabe 8.2
# a)
# Gepaart
# einseitig
# H0: uR = uNR
# Ha: u > median.alt

# b)
# geppaart
# einseitig
# H0: FBp = EBp
# HA: FBp > EBp

# c)
# ungepaart
# zweiseitig
# H0: uV = uK
# HA: uV =! uK

# d)
# ungepaart
# einseitig
# H0: uFe2 = uFe3 
# HA: uFe2 =! uFe3

# Aufgabe 8.3
# a)
# Gepaart

# b)
from scipy.stats import t
# T-Test
# Modellannahmen = o = 6.2
# N0: ua = ub
# Na: ub > ua
# Teststatistik: t Verteilung mit Freiheitsgrad 8
# Signifikanzniveau: a = 5%
# Verwerfungsbereich:
t.ppf(q=0.05, df=8, loc=0, scale=6.2/np.sqrt(9))
# Testentschieid:
    # Der Wert ist dn= -5.78
    # Das heisst die Geräte weichen zu sehr ab
    
# c)
# TODO

# Aufgabe 8.4
# a)
# Gepaart

# b)
# einseitig

# c)
# N0: u1 = u2
# NA: u1 > u2

# d)
# T-Test
t1 = pd.Series([39.1, 39.3, 38.9, 40.6, 39.5, 38.4, 38.6, 39.0, 38.6, 39.2])
t2 = pd.Series([38.1, 38.3, 38.8, 37.8, 38.2, 37.3, 37.6, 37.8, 37.4, 38.1])

st.ttest_rel(t2, t1).pvalue / 2


# e)
st.wilcoxon(t1,t2, alternative="greater")

# f)

# Aufgabe 8.5
# a)
# ungepaart

# b)
# H0: uM = uW
# HA: uM != uW

# c)
jackals = pd.read_table(r"jackals.txt", sep = " ")
jackals
st.ttest_ind(jackals["M"], jackals["W"], equal_var=False)

# d)
st.mannwhitneyu(jackals["M"],jackals["W"], alternative="two-sided")

# Aufgabe 8.6
# a)
zurich = pd.Series([16.3, 12.7, 14.0, 53.3, 117, 62.6, 27.6])
basel = pd.Series([10.4, 8.91, 11.7, 29.9, 46.3, 25.0, 29.4])

d = zurich - basel
u = np.mean(d)
o = d.std()
u
o


# b)
# ungepaart

# c)
# H0: uZ = uB
# HA: uZ > uB

# d)
st.ttest_ind(zurich, basel, equal_var=False)

# e)
st.mannwhitneyu(zurich, basel, alternative="greater")

# Aufgabe 8.7
# a)
# ungepaart

# b)
# zweiseitiger test

# c)
# H0: uR = uG
# HA: uR != UR

# d)
rind = pd.Series([186, 181, 176, 149, 184, 190, 158, 139, 175, 148, 152, 111, 141, 153, 190, 157, 131, 149, 135, 132])
geflugel = pd.Series([129, 132, 102, 106, 94, 102, 87, 99, 170, 113, 135, 142, 86, 143, 152, 146, 144])

r = rind.mean()
g = geflugel.mean()

#  e)
# wilcoxon weil nicht normalverteilt

# f)
st.mannwhitneyu(rind, geflugel)


# Aufgabe 8.8
# a)
import pandas as pd
mf <- pd.read_csv(r"mannfrau.csv")



































