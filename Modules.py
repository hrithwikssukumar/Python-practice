

# Importing module by calling the name

import Mathoperation
print(Mathoperation.a)
print(Mathoperation.cube(8))
print(Mathoperation.calculator(5,4))


# Importing module using *

from Mathoperation import *
print(a)
print(cube(9))
print(calculator(8,5))


# Importing module by renaming the module name
import Mathoperation as m
print(m.a)
print(m.cube(4))
print(m.calculator(8,4))



    