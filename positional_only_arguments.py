'''
A positional argument is a name that is not followed by an equal sign (=)
and default value. A keyword argument is followed by an equal sign and an
expression that gives its default value.

Positional-only parameters give more control to library authors to better
express the intended usage of an API and allows the API to evolve in a safe,
backward-compatible way. Additionally, it makes the Python language more
consistent with existing documentation and the behavior of various "builtin"
and standard library functions.
'''

'''
In Python 3.8, you can use / to denote that all arguments before it must be 
specified by position. You can rewrite incr() to only accept positional 
arguments.
'''

def incr(x, /):
    return x+1

#print(incr(x=3.8))
#print(incr(3.8))

'''
Traceback (most recent call last):
  File "positional_only_arguments.py", line 22, in <module>
    print(incr(x=3.8))
TypeError: incr() got some positional-only arguments passed as keyword arguments: 'x'
'''

'''
To combine regular arguments with the positional arguments, use them post / 
'''
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Christopher"))
#Hello, Christopher

print(greet("Christopher", greeting="Awesome job"))
#Awesome job, Christopher

#print(greet(name="Christopher", greeting="Did it work?"))
#Traceback (most recent call last):
#  File "positional_only_arguments.py", line 40, in <module>
#    print(greet(name="Christopher", greeting="Did it work?"))
#TypeError: greet() got some positional-only arguments passed as keyword arguments: 'name'

'''
Similarly, arguments after * should be only keyword arguments. 
'''
def headline(text, /, border="~", *, width=50):
    return f" {text} ".center(width, border)

print(headline("Positional-only Arguments"))
#~~~~~~~~~~~ Positional-only Arguments ~~~~~~~~~~~~

print(headline("Positional-only Arguments", border=":"))
#::::::::::: Positional-only Arguments ::::::::::::

print(headline("Positional-only Arguments", "@"))
#@@@@@@@@@@@ Positional-only Arguments @@@@@@@@@@@@


#References:
#https://www.python.org/dev/peps/pep-0570/
#https://www.python.org/dev/peps/pep-0457/