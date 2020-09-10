# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:50:53 2020

@author: freya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pres = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW02\Übungen\president.csv", index_col=0)

#Serie 2
#Aufgabe2.1
#a) Index = Key value prinzip --> Jahr wird zum Index sonst wird Index hinzugefügt
print(pres.head())

#b)
print(pres.shape)

#c)
pres.loc[[1996,1992], "Height_win"] = 189
print(pres)

#d)
pres.mean()

#e)
diff = pres["Height_win"] - pres["Height_opp"]
diff.mean()

#Aufgabe2.2
#a)
a = pd.Series([4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 5.2, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1])
a.median()
a.mean()
a.sort_values()
a.size
b = pd.Series([4.2, 2.3, 5.6, 4.65, 4.65, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 200, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1])
b.median()
b.mean()
b.sort_values()

#b)
a = pd.Series([4.2, 2.3, 5.6, 4.5, 4.8, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 5.2, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1])
b = pd.Series([4.2, 2.3, 5.6, 4.65, 4.65, 3.9, 5.9, 2.4, 5.9, 6, 4, 3.7, 5, 200, 4.5, 3.6, 5, 6, 2.8, 3.3, 5.5, 4.2, 4.9, 5.1])

plt.subplot(221)
a.plot(kind="box")
plt.subplot(222)
b.plot(kind="box")
plt.subplot(223)
a.plot(kind="hist",edgecolor="black")
plt.subplot(224)
b.plot(kind="hist",edgecolor="black")
plt.show()

#Aufgabe2.3
#a)
couples = pd.read_csv(r"husband_wive.csv")
couples.head()
print(couples)

# b) Mit der Methode .describe() erhalten wir eine kurze statistische Übersicht
# über die Daten. Es wird die Anzahl der Daten aufgeführt (count), der Mittelwert
# (mean), die Standardabweichung (std), der kleinste Wert (min), das untere
# Quartil (25%), der Median (50%), das obere Quartil (75%) und der maximaleWert
# (max).
couples.describe()

# c)
diff = couples["age.husband"] - couples["age.wive"]
diff.plot(kind="box")

# Aufgabe 2.4
# a)
schlamm = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW02\Übungen\klaerschlamm.dat", sep=" ", index_col=0)
schlamm = schlamm.drop("Labor",1)
schlamm.head()

schlamm.describe()

schlamm.plot(kind="box")
mean = schlamm.mean()
median = schlamm.median()

# b)
messfehler = schlamm - schlamm.median()
messfehler.T.plot(kind="box")

# Aufgabe2.5
# a)
# 1b
# 2c
# 3a





























