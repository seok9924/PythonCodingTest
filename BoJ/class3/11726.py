import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

