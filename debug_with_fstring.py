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


# Additoinal References:
#https://realpython.com/python-f-strings/