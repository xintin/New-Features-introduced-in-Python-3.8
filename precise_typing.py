'''
Python 3.8 provides some new features to allow more precise typing.
There are four new PEPs about type checking that have been accepted
and included in Python 3.8:

    Literal types
    Typed dictionaries
    Final objects
    Protocols

Type Hinting: Type hinting is a formal solution to statically indicate
              the type of a value within your Python code.


'''

def double(number:float) -> float:
    return 2*number

print(double(3))
#6

#print(double("This should not be accepted"))
#This should not be acceptedThis should not be accepted

'''
As we could see, it is accepting string also as a float type.
On using static type checker like mypy we get the below error
for the above statement. 

precise_typing.py:20: error: Argument 1 to "double" has incompatible type "str"; expected "float"
Found 1 error in 1 file (checked 1 source file)
'''


'''
LITERALS

If we do not use Literal from typing, the static type checker will fail to identify
that UP is not a valid direction. Since it is still a string datatype, it will pass. 
'''

from typing import Literal

def draw_line(direction: Literal["horizontal", "vertical"]) -> None:
    if direction == "horizontal":
        ...  # Draw horizontal line

    elif direction == "vertical":
        ...  # Draw vertical line

    else:
        raise ValueError(f"invalid direction {direction!r}")

#draw_line("up")
draw_line("horizontal")



'''
In the below example the added @overload signatures will help your type checker 
infer str or int depending on the literal values of to_roman. Note that the 
ellipses (...) are a literal part of the code. They stand in for the function 
body in the overloaded signatures. Here, one would like the type checker to infer 
exactly whether str or int is returned. This can be done using Literal together 
with @overload:
'''

from typing import Literal, overload, Union

ARABIC_TO_ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
                   (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
                   (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

def _convert_to_roman_numeral(number: int) -> str:
    """Convert number to a roman numeral string"""
    result = list()
    for arabic, roman in ARABIC_TO_ROMAN:
        count, number = divmod(number, arabic)
        result.append(roman * count)
    return "".join(result)

@overload
def add(num_1: int, num_2: int, to_roman: Literal[True]) -> str: ...
@overload
def add(num_1: int, num_2: int, to_roman: Literal[False]) -> int: ...

def add(num_1: int, num_2: int, to_roman: bool = True) -> Union[str, int]:

    result = num_1 + num_2

    if to_roman:
        return _convert_to_roman_numeral(result)
    else:
        return result

print(add(1,2,False))
print(add(1,2,True))


'''
FINAL 

This qualifier specifies that a variable or attribute should not be reassigned, 
redefined, or overridden. 

Additionally, there is also a @final decorator that can be applied to classes and methods. 
Classes decorated with @final can’t be subclassed, while @final methods can’t be overridden 
by subclasses
'''

from typing import Final, final

ID: Final = 1
#ID += 1 #will throw an error

@final
class Base:
    pass

#class Sub(Base):
#    pass
#error: Cannot inherit from final class "Base"


'''
TypedDict

This can be used to specify types for keys and values in a dictionary using a 
notation that is similar to the typed NamedTuple. A dict can store only one type
of keys and only one type pf values whereas a TypedDict can have varying datatypes
for the values.

During runtime a TypedDict is a regular dict, and type hints are ignored as 
usual. 
'''

from typing import TypedDict

class PythonVersion(TypedDict):
    version: str
    release_year: int

py38 = PythonVersion(version="3.8", release_year=2019)


'''
PROTOCOL

Protocols are a way of formalizing Python’s support for duck typing.
Duck typing allows you to, for example, read .name on any object that 
has a .name attribute, without really caring about the type of the 
object. It may seem counter-intuitive for the typing system to support this. 
'''

'''
errored code

from typing import Protocol

class Named(Protocol):
    name: str

def greet(obj: Named) -> None:
    print(f"Hi {obj.name}")

class Dog:
    pass

x = Dog()

greet(x)

run: mypy precise_typing.py
error: Argument 1 to "greet" has incompatible type "Dog"; expected "Named"
'''



'''
If the Dog class is not having an attribute of .name, it will not meet the check 
for the Named protocol. Add a .name attribute to the class, with a default string
to make mypy pass. 
'''

from typing import Protocol

class Named(Protocol):
    name: str

def greet(obj: Named) -> None:
    print(f"Hi {obj.name}")

class Dog:
    name = 'Good Dog'

x = Dog()

greet(x)



#https://realpython.com/lessons/type-hinting/
#https://www.python.org/dev/peps/pep-0484/
#https://www.python.org/dev/peps/pep-0591/
#https://www.python.org/dev/peps/pep-0589/
#https://www.python.org/dev/peps/pep-0544/