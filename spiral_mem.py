"""
Owen Sullivan
"""
from math import *


def find_distance(value):
    root = sqrt(value)
    corner = 0
    if (root+1) % 2 == 0:
        return root-1
    elif (int(root)+1) % 2 != 0:
        root = int(root)+1
        corner = root**2
        diff = corner-value
        while True:
            if diff<root:
                if diff<root//2:
                    diff-= root//2
                    break
                else:
                    break
            else:
                diff-= root
        return root-diff-1


print(find_distance(24))












