import sys
import unittest

from argparser import Argparser

argv_list = sys.argv

AP1 = Argparser(argv_list)

print(AP1.option)
print(AP1.flags)
print(AP1.pos)

