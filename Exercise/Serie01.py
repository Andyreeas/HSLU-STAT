# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:57:29 2020

@author: freya
"""
import numpy as np
import pandas as pd

#Serie 1
#Aufgabe1.1
#a)
x = pd.array([4,2,1,3,3,5,7])
y = pd.Series([4,5,6])

#b)
x[2]

#c)
x[[0,3]]

#d)
x.size

#e)
print(x+2)

#f)
np.sum(x+2)

#g)
#Boolen Werte für alle Index auf die, die Bedingung zutrifft
x <= 3

#h)
x[x <= 3]

#i)
np.sort(x)

#j)
np.argsort(x)

np.argsort(x) +1
#k)
x[3] = 8

#Aufgabe 1.2
#a)
fahrenheiten = pd.Series([51.9, 51.8, 51.9,53])
#b)
celsius = pd.Series((5/9)*(fahrenheiten - 32))
celsius
#c)
fahrenheitenneu = pd.Series([48, 48.2, 48, 48.7])
fahrenheiten - fahrenheitenneu

#Aufgabe 1.3
#a)
weight = pd.Series([60,72,57,90,95,72])
height = pd.Series([1.75, 1.80, 1.65, 1.90, 1.74, 1.91])

#b)
bmi = weight/height**2

#Aufgabe1.4
#a)
data = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW01\Übungen\weather.csv", sep=",")
print(data)
#b)
print(data.loc["Apr", "Chur"])
#c)
print(data.loc["Apr"])
#d)
print(data.loc[:,["Luzern","Zurich"]])
#e)
data1 = data.loc[:,["Luzern","Zurich"]]
data1.to_csv("../../../Software_R_Python/Python/weather2.csv")
#f)
print(data.columns.values)
#g)
data.columns.values[1] = "Genf"
print(data.columns.values)
#h)
data = data.sort_values(by= "Zurich")
#i)
data = data.sort_values(by="Zurich", ascending = False)

#Aufgabe1.5
#a)
from pandas import Series,DataFrame
import pandas as pd
data = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\Übungen\child.csv", sep=",", index_col=0)
print(data)
#b)
data.shape
#c)
data.describe()
#d)
data.index
"China", "China" in data.index
"Netherlands", "Netherlands" in data.index
data.columns
#e)
drunk = data.sort_values(by="Drunkenness", ascending = False)
drunk["Drunkenness"].head()

"""
Denmark           24.8
Finland           22.4
United Kingdom    22.1
Poland            19.9
Canada            18.8
Name: Drunkenness, dtype: float64
"""

data.loc["Denmark","Drunkenness"]

#f)
infantmortality = data.nsmallest(n=1, columns="Infant.mortality")
infantmortality.index

#g)
durbewe = data["Physical.activity"].mean()
data.loc[data["Physical.activity"] < durbewe,:].index

#Aufgabe1.6
#a)
import pandas as pd
from pandas import DataFrame, Series
fuel = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\SW01\Übungen\d.fuel.dat", sep=",", index_col=0)
#b)
fuel.loc[5]
#c)
fuel.loc[1:5]
#d)
fuel["mpg"].mean()
#e)
fuel.loc[7:22,"mpg"].mean()
#f)
t_kml = fuel["mpg"]*1.6093/3.789
t_kml
t_kg = fuel["weight"]*0.45359
t_kg
#g)
t_kml.mean()
t_kg.mean()








