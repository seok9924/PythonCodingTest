import math

import itertools
import collections
import heapq
import functools
import re
import bisect
from collections import deque
import os

import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


def star(n):
    if n==3:
        return ["***","* *","***"]

    arr=star(n//3)
    stars=[]

    for i in arr:
        stars.append(i * 3)

    for i in arr:
        stars.append(i + ' ' * (n // 3) + i)

    for i in arr:
        stars.append(i * 3)

    return stars

n=int(input())
print('\n'.join(star(n)))