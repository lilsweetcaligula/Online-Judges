#!/bin/python3

import sys

fact = lambda n: 1 if n <= 1 else n * fact(n - 1)

n    = int(input().strip())
fct  = fact(n)

print(fct)
