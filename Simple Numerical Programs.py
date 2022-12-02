#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:19:44 2022

@author: stoner69
"""

#Exercise
print("Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.")
var_ = int(input("Enter an integer: "))
pwr = 5
root = 0
while root**pwr <= var_:
    print("root={}, pwr={}".format(root, pwr))
    print("root**pwr =", root**pwr)
    if root**pwr == var_:
        break
    else:
        root += 1
print("loop over")
if root**pwr == var_:
    print("root = {}, pwr = {} and root**pwr = {}".format(root, pwr, var_))
else:
    print("no integer pair exist such that number1**number2 == the entered integer")