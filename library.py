# note the _ character
population = 9_700_000
log(population)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'log' is not defined
'''
import math
log(population)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'log' is not defined
'''
# log() still not defined, we have to reach into the math library
math.log(population)
# 16.08763644347361
math.log(2.71)
# 0.9969486348916096
from math import log
log(population)

### DANGER ZONE
def log(x):
    # a crude approximation
    return x - 1
log(2.7)
# 1.7000000000000002
from math import *
log(2.7)
# 0.9969486348916096
## the import has SILENTLY overwritten our carefully crafted log function