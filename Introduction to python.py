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

#--------------------------------


#nested if-else
print('\n#Nested if else')
print('x =', x)
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')

#--------------------------------


#compound Boolean expresssion
print('\nCompound Boolean expression')
x, y, z = 10, 2, 8
print('x, y, z = 10, 2 , 8')
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')