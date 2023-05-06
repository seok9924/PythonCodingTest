
import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

br = "([)]"
mp = {c:i for i,c in enumerate(br)}

def solve(s):
    a = []
    for c in s:
       if c in mp:
            if c in br[:2]: a.append(c)
            else:
                if a and mp[c]-mp[a[-1]]==2:
                    a.pop()
                else:
                    print('no')
                    return
    if a: print('no')
    else: print('yes')

while 1:
    s = input()
    if s=='.': break
    solve(s)

