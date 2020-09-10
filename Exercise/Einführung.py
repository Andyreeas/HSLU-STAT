# -*- coding: utf-8 -*-

"""
Spyder Editor

Dies ist eine temporäre Skriptdatei.
"""

import numpy as np

print("Hello World!")
# Hello World!

a = 3
b = 4
a + b
# 7

a, b = 3, 4
a + b
# 7

np.sqrt(2)
# 1.4142135623730951

x = np.array([2, 1, 4, 5, -8])
x
# [ 2 1 4 5 -8]

3*x
# [ 6 3 12 15 -24]

x*x
# [ 4 1 16 25 64]

x = np.linspace(start=1, stop=2, num=4)
x
## [1. 1.33333333 1.66666667 2. ]

import pandas as pd
from pandas import Series, DataFrame
temp_luz = Series([1, 5, 9, 15, 20, 25, 25])
temp_luz

temp_luz = Series(
[1, 5, 9, 15, 20, 25, 25],
index=("jan", "feb", "mar", "apr", "mai", "jun", "jul")
)
temp_luz

temp = DataFrame({
"Luzern": ([1,5,9,15,20,25,25]),
"Basel": ([3,4,12,16,18,23,32]),
"Zuerich": ([8,6,10,17,23,22,24])},
index=["jan","feb","mar","apr","mai","jun","jul"]
)
temp

temp.mean()

child = pd.read_csv(r"C:\Users\freya\OneDrive\HSLU\6. Semester 2020FS\STAT\Übungen\child.csv", sep=",")
print(child)




























