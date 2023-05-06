
import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")
import math
a,b,v = map(int,input().split())

t= (v-b)/(a-b)

print(math.ceil(t))