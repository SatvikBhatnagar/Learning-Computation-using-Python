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
    
#--------------------------------
#--------------------------------

##Exercise
print('Write a program that examines three variables- x, y, and z - and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.')
x, y, z = 4, 7, 9
print('x, y, z = 4, 7, 9')
if x%2 == 1:
    if y%2 == 1:
        if x > y:
            if z%2 == 1:
                if x > z:
                    print('x is the largest odd number')
                else:
                    print('z is the largest odd number')
            else:
                print('x is the largest odd number')
        else:
            print('y is the largest odd number')
    elif z%2 == 1:
        if x > z:
            print('x is the largest odd number')
        else:
            print('z is the largest odd number')
    else:
        print('x is the largest odd number')
elif y%2 == 1:
    if z%2 == 1:
        if y > z:
            print('y is the largest odd number')
        else:
            print('z is the largest odd number')
    else:
        print('y is the largest odd number')
elif z%2 == 1:
    print('z is the largest odd number')
else:
    print('x, y, z are not odd numbers')
    
#--------------------------------
#--------------------------------

#type checking
print('\n#type checking')
a = 5
print('a = 5 ---> type =',type(a))
b = 'c'
print("b = 'c' ---> type =", type(b))

#--------------------------------

#length, indexing and slicing
print('\n#pritning length of a string')
print("STRING - 'Heyaa'")
print('length of the strihng is:', len('Heyaa'))

print("\n#printing the character at the index 3 in the string 'abc'")
print("3rd charachter in the string 'abc' is:", 'abc'[2])

print("\n#Slicing the string 'Hi!, how are you?' from the 5th index")
print('--->' + 'Hi!, how are you?'[4:])