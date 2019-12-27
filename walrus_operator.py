import os

'''
Since it resembles the eyes and tusk of a walrus.
It allows to assign and return the value in the same expression.
'''


flag = True
print(flag)


#print(flag=False)
'''
Traceback (most recent call last):
  File "walrus_operator.py", line 11, in <module>
    print(flag=False)
TypeError: 'flag' is an invalid keyword argument for print()
'''

print(flag := False)
#False

inputs = list()

#loop 1
while True:
    current = input("Write Something: ")
    if current == "quit":
        break
    inputs.append(current)

#loop 2
while (current := input("Write something: ")) != "quit":
    inputs.append(current)

print(inputs)


#Other Examples

#Python3.7
env_base = os.environ.get("PYTHONUSERBASE", None)
if env_base:
    print(env_base)

#Python 3.8
if env_base := os.environ.get("PYTHONUSERBASE", None):
    print(env_base)




#References:
#https://www.python.org/dev/peps/pep-0572/
#https://www.python.org/dev/peps/pep-0572/#examples