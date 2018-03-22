## 1. Introduction to Modules ##

import math
root = math.sqrt(99)
flr = math.floor(89.9)

## 2. Importing Using An Alias ##

"""
n the last step, we learned that we can import an entire module using the import statement. When we import a module this way, we add all of the objects and functions within that module to the global namespace. A namespace is a dictionary that contains all of the names we can refer to in our code. Before running our code, the Python interpreter adds all of the objects and functions that are available by default (print(), list(), etc.) to the global namespace. When we create variables or define our own functions, these are also added to the same namespace.
"""
import math as m
root = m.sqrt(33)



## 3. Importing A Specific Object ##

from math import *
from math import sqrt
root = sqrt(1001)

## 4. Variables Within Modules ##

import math

a = math.sqrt((math.pi))
b = math.ceil((math.pi))
c = math.floor((math.pi))

## 5. The CSV Module ##

import csv
f = open("nfl.csv")
csvreader = csv.reader(f)
nfl = list(csvreader) # defining moment to convert a file to the list directly

## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv", "r")
nfl = list(csv.reader(f))
patriots_wins = 0

for i in nfl:
    if i[2] == "New England Patriots":
        patriots_wins += 1

patriots_wins


## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(teamname):
    wincnt = 0
    for i in nfl:
        if i[2] == teamname:
            wincnt += 1
    return wincnt

cowboys_wins = nfl_wins("Dallas Cowboys")
print(cowboys_wins)
falcons_wins = nfl_wins("Atlanta Falcons")
print(falcons_wins)
    
    