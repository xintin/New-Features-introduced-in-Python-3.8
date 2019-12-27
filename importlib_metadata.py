'''
A new module!

Through this module, one can access information about installed packages
in Python installation. Together with its companion module, importlib.resources,
importlib.metadata improves on the functionality of the older pkg_resources.
metadata() gives access to most of the information that you can see on PyPI.
'''

from importlib import metadata

print(metadata.version("pip"))
#19.3.1

pip_metadata = metadata.metadata("pip")
print(list(pip_metadata))
#['Metadata-Version', 'Name', 'Version', 'Summary', 'Home-page', 'Author', 'Author-email',
# 'License', 'Description', 'Keywords', 'Platform', 'Classifier', 'Classifier', 'Classifier',
# 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier',
# 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Classifier', 'Requires-Python']


print(pip_metadata["Home-page"])
#https://pip.pypa.io/


print(pip_metadata["Requires-Python"])
#>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*
#It requires either Python2.7 or 3.5 and higher



'''
files() returns a list of Path objects. These give one a convenient way of looking into the 
source code of a package, using read_text(). The following example prints out __init__.py 
from the math package.
'''

print(temp := [p for p in metadata.files("mypy") if p.suffix == ".py"])

print(temp[10]) #mypy/checkmember.py
init_path = temp[10] #_[0]

print(init_path.read_text())
#You will see the source code of the mypy/checkmember.py package.
#"""Type checking of attribute access"""
#from typing import cast, Callable, Optional, Union, List
#from typing_extensions import TYPE_CHECKING
#...



#To access package dependencies
print(metadata.requires("mypy"))
#['typed-ast (<1.5.0,>=1.4.0)', 'typing-extensions (>=3.7.4)',
# 'mypy-extensions (<0.5.0,>=0.4.3)', "psutil (>=4.0); extra == 'dmypy'"]


#Additional References
#https://importlib-metadata.readthedocs.io/en/latest/