#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 03:01:44 2019

@author: bl
"""
# Calculator

1+7


2*4



# A first example
1+1

"""
A first example 
with a longer comment
"""

1+1

3 + 4


# Assignments

a = 3
bb = 4

a


bb

a, bb = 3, 4


2.7 * a


# The exponation operator is ** in Python instead of ^ as in most other programming languages 
a**2


a/bb



a = 7

a

A



a = 3
3a


# Simple lists

z_1 = [3, 4, 4.5, -2, 7]

z_1

z_2 = [1, 2, 3, 4, 5]

z_2

mixed = [2, 'sad', 5.3, 'YES', "beautiful", "sad"]

mixed


# module numpy


import numpy

numpy.sqrt(2)


import numpy as np

np.sqrt(2)



from numpy import sqrt

sqrt(2)



# Vectors

import numpy as np

x = np.array([2, 1, 4, 5, -8])

x

3*x

x = np.array([2,1,4,5,-8])

x*x



x = np.linspace(start=1, stop=2)

x


y = np.arange(start=1, stop=7, step=.6)

y


z = np.arange(start=2, stop=9)

z


w = np.arange(9)

w






# module pandas



import pandas as pd
from pandas import Series, DataFrame

temp_luz = Series([1, 5, 9, 15, 20, 25, 25])

temp_luz


temp_luz[2]


temp_luz = Series(
    [1, 5, 9, 15, 20, 25, 25],
    index=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul")
)

temp_luz

temp_luz["Mar"]



# First statistical applications

temp_luz.index

temp_luz.size


temp_luz.min()

temp_luz.mean()



temp_luz.sum()




temp_luz["Jun"]

temp_luz["Jan":"May"]

temp_luz[["Jan","May"]]


# commands with options
z_3 = Series([5, 2, np.nan, 4])
z_3



z_3.min()



z_3.min(skipna=True)










# datasets (two-dimensional)



temp = pd.read_csv("weather.csv")

temp


"""
windows

temp = pd.read_csv(r"C:\Users\Documents\folder\Python\weather.csv")
"""


temp.head()



temp = pd.read_csv("weather.csv", sep=";")



# slicing
temp = pd.read_csv("weather.csv")
temp.columns

temp.mean()

temp.mean(axis=1)

temp.min(axis=1)

temp["Luzern"]

temp.loc[:, "Luzern"]

temp.loc["Apr":"Jun", :]

temp.loc["Apr":"Jun", "Luzern"]

temp.loc["May", "Zurich"]

temp.loc[["Apr", "Jun"], ["Basel", "Zurich"]]



# Operationens with datasets

temp.plot()



temp.plot(kind="box")

temp.median()






