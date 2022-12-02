#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:19:44 2022

@author: stoner69
"""

#Exercise
print("Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.")
var_ = int(input("\nEnter an integer: "))
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
    
#---------------------------------------------
#for loop
print("\n")
x = 4
for i in range(x):
    print(i)
    x=5 #this doesn't changes the value of x globally because -the arguments to the range fucntion in the line with for are ecaluated just before the first iteration of the loop, and not reevaluated for subsequent iterations

print("\n")
x = 4
for j in range(x):
    for i in range(x):
        print(i)
        x=2 #this does not change the x for the 'j' loop, but wherenver the 'i' loop started, it revaluates everytime
        
#---------------------------------------------
print("\nFinding cube root of a perfect cube")
x = int(input("Enter an integer: "))
for ans in range(0, abs(x)+1):
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)