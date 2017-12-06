
def find_diff(st):
    big = int(st[0])
    small = int(st[0])
    for c in st:
        if int(c) > big:
            big = int(c)
        if int(c) < small:
            small = int(c)
    return big-small


def find_div(lst):
    lst2 = lst[:]
    for e in lst:
        for num in lst2:
            if e == num:
                pass
            elif (int(e) % int(num) == 0):
                return int(e) / int(num)



def add_total(fd):
    total = 0
    for line in fd:
        line = line.split()
        temp = find_div(line)
        print(temp)
        total += temp
    return total

fd = open("help.txt")
print(add_total(fd))






