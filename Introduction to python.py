# -*- coding: utf-8 -*-

#Variables, assigning and printing
pi = 3
radius = 11
area = pi * (radius**2)
print(area)

#--------------------------------


#multiple assignments
x, y = 2, 3
x, y = y, x
print('x =', x)
print('y = ', y)

#--------------------------------


#if-else conditionals
print('\n#Conditionals')
if x%2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')