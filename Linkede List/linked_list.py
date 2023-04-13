import math
import sys
from os import path
import itertools
import collections
import heapq
import functools
import re
import bisect
from collections import deque
import os

class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next

first = Node(value=1)
second= Node(value=2)
third = Node(value=3)
first.next= second
second.next= third

first.value=6
print(first.value)

class LinkedList(object):
    def __init__(self):
        self.head=None

    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else :
            current=self.head
            while(current.next):
                current=current.next
            current.next=new_node

    def get(self,idx):
        current= self.head
        for i in range(idx):
            current=current.next
        return current.value

    def insert(self,idx,value):
        new_node=Node(value)
        current= self.head
        if idx==0 :
            self.head= new_node
            self.head.next=current
        else:
            for i in range(idx-1):
                current=current.next
            tmp=current.next
            current.next=new_node
            new_node.next=tmp
    def remove(self,idx):
        current=self.head

        if idx==0:
            self.head=current.next


        for i in range(idx-1):
            current=current.next
        current.next=current.next.next
        