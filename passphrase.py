import math


def passphrase(lst):
    dic = {}

    for e in lst:
        if e in dic:
            return 0
        else:
            dic[e] = 1
    return 1

def anagram(lst):
    dic = {}

    for e in lst:
        e = ''.join(sorted(e))
        if e in dic:
            return 0
        else:
            dic[e] = 1
    return 1
       





def add_total(fd):
    total = 0
    for line in fd:
        line = line.split()
        temp = anagram(line)
        total += temp
    return total





fd = open("help.txt")
print(add_total(fd))






