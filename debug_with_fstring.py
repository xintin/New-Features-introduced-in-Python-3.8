'''
In Python 3.8, we can use assignment operator inside f-strings. 
Remember to surround them with the parenthesis.
'''

import math

r = 3.8

print(f"Diameter {(diam:=r)} gives circumference {math.pi*r*2:.2f}")

#Now, to debug just add = in the end as shown below
print(f"{r=}")
#r=3.8

#One can add spaces around =, and use format specifiers
name = "ERIC"

print(f"{name.upper()[::-1] = }")
#name.upper()[::-1] = 'CIRE'

print(f"{name = :>10}")
#name =       ERIC


'''
Python has a SyntaxWarning that can warn you about dubious syntax 
that is typically not a SyntaxError.

Example: Python 3.8 will try to warn you about cases when one should
         use == instead of is
'''

#in REPL
#version = "3.7"
#versoin is "3.7"
#<input>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?

'''
Now missing a comma in a tuple will show a warning along with the error
'''
#[(3,5),(1,2)]
#[(3, 5), (1, 2)]
#[(3,5)(1,2)]
#<input>:1: SyntaxWarning: 'tuple' object is not callable; perhaps you missed a comma?
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#TypeError: 'tuple' object is not callable







# Additoinal References:
#https://realpython.com/python-f-strings/