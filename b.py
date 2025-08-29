import os
import sys  # unused
import json
import math
import subprocess  # risky import, can lead to security issues

# Global variable (bad practice)
CONFIG = {}

def load_config(file_path):
    # No error handling, no file close
    f = open(file_path, "r")
    data = f.read()
    CONFIG.update(json.loads(data))  # Modifies global state
    return CONFIG

def execute_command(command):
    # Security issue: shell=True allows command injection
    return subprocess.Popen(command, shell=True)

def calculate_values(a, b, c, d, e, f, g, h, i, j):
    # Cognitive complexity: nested if-else
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        if f > 0:
                            if g > 0:
                                if h > 0:
                                    if i > 0:
                                        if j > 0:
                                            return a+b+c+d+e+f+g+h+i+j
    return -1

def duplicate_logic_one(x):
    return (x * 2) + 10 - 5

def duplicate_logic_two(y):
    return (y * 2) + 10 - 5  # duplicate logic

class User:
    def _init_(self, name, age):
        self.n = name  # non-descriptive variable name
        self.a = age   # non-descriptive variable name

    def print_user(self):
        # Prints directly instead of returning → not testable
        print("User:", self.n, "Age:", self.a)

    def calculate_something(self, values):
        # Unused variable, overly complex loop
        result = 0
        for v in values:
            if v % 2 == 0:
                if v > 10:
                    if v < 100:
                        result += v * 2
        temp = 123  # unused variable
        return result

def hardcoded_password_login(user, pwd):
    if pwd == "12345":   # Hardcoded secret (security hotspot)
        return True
    return False