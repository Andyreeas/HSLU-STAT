# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:05:58 2020

@author: freya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Serie 3
# Aufgabe 3.1
# a)
hubble = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW03\Übungen\hubble.txt", sep=" ")
hubble.plot(kind="scatter",
            x="recession.velocity",
            y="distance")

# b)
beta1, beta0 = np.polyfit(y=hubble["distance"],
                          x=hubble["recession.velocity"],
                          deg=1)
print(beta1, beta0)

x = np.linspace(hubble["recession.velocity"].min(),
                hubble["recession.velocity"].max())
plt.plot(x, beta0 + beta1*x, color="orange")
plt.show()

# c)
hubble.corr()

# Aufgabe 3.2
# a)
income = pd.read_csv("income.dat", sep=" ")
income
income.plot(kind="scatter",
            x="Educ",
            y="Income2005")

income.plot(kind="scatter",
            x="AFQT",
            y="Income2005")

# b)
income.plot(kind="scatter",
            x="Educ",
            y="Income2005")
x = np.linspace(income["Educ"].min(), income["Educ"].max())
a, b = np.polyfit(income["Educ"], income["Income2005"], deg=1)
plt.plot(x,a*x+b,c="orange")

income.plot(kind="scatter",
            x="AFQT",
            y="Income2005")
x = np.linspace(income["AFQT"].min(), income["AFQT"].max())
a, b = np.polyfit(income["AFQT"], income["Income2005"], deg=1)
plt.plot(x,a*x+b,c="orange")

# c)
income.corr()

# Aufgabe 3.3
# a)
x1 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

test1 = pd.DataFrame({
        "x":([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]),
        "y":([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
        })

test1.plot(kind="scatter",
          x="x",
          y="y")

x = np.linspace(x1.min(), x1.max())
a, b = np.polyfit(x1, y1, deg=1)
plt.plot(x,a*x+b,c="orange")

test2 = pd.DataFrame({
        "x":([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]),
        "y":([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
        })

test2.plot(kind="scatter",
          x="x",
          y="y")

x = np.linspace(x1.min(), x1.max())
a, b = np.polyfit(x1, y1, deg=1)
plt.plot(x,a*x+b,c="orange")

# b)
np.polyfit(x1, y1, deg=1)
np.polyfit(x1, y2, deg=1)
np.polyfit(x1, y3, deg=1)
np.polyfit(x4, y4, deg=1)

test1.corr()
test2.corr()

# c)
np.corrceof(x1, y1)

# Aufgabe 3.4
# a)
# xi Elementarereignis abs. Häufigkeit pi
# 2 11 1 
# 3 12,21 2
# 4 13,22,31 3 
# 5 14,23,32,41 4 
# 6 15,24,33,42,51 5 
# 7 16,25,34,43,52,61 6 
# 8 26,35,44,53,62 5 
# 9 36,45,54,63 4 
# 10 46,55,64 3 
# 11 56,65 2 
# 12 66 1 

# b)

x = np.arange(2, 13)
p = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) / 36
np.sum(x * p)

# Aufgabe 3.5
p2 = 1 - 0.3 - 0.1 - 0.2 - 0.3
x = pd.Series([-5, -4, 1, 3, 6])
y = pd.Series([0.3, p2, 0.1, 0.2, 0.3])
np.sum(x * y)






































