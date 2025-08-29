import os
import sys   # unused import

def add(a, b): 
    return a + b

def addition(a, b):   # duplicate function
    return a + b

def BADfunction(x,y):  # bad naming convention
    result = x + y
    return result

def file_reader(filepath):
    f = open(filepath)   # file not closed → resource leak
    data = f.read()
    return data

def complex_function(a, b, c, d, e, f, g):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        if f > 0:
                            if g > 0:
                                return a+b+c+d+e+f+g
    return 0