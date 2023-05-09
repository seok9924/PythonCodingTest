
import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

import sys
n=int(sys.stdin.readline())


def operations(oper,number,numdict):

    if oper=='add':
        numdict[number]=1
    if oper=="check":
        if number in numdict:
            print(1)
        else:
            print(0)
    if oper=="remove":
        if number in numdict:
            del numdict[number]

    if oper=="toggle":
        if number in numdict:
            del numdict[number]
        else:
            numdict[number]=1
    if oper=="all":
        for i in range(1,21):
            numdict[i]=1

    if oper=="empty":
        numdict={}

    return numdict


d={}

for i in range(n):
    original=sys.stdin.readline()
    if original=='all' or original=='empty':
        oper=original
        number=-1
    else:
        oper,number=original.split()

    d=operations(oper,int(number),d)
