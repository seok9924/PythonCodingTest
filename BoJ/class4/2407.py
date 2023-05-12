from collections import deque
import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

import math
n,m=map(int,input().split())

a=math.factorial(n)
b=(math.factorial(n-m))*(math.factorial(m))
print(a//b)
