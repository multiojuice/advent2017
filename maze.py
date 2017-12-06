

def move(lst):
    count = 0
    idx = 0
    move = 0
    while(idx+move < len(lst) and idx+move >=0):
        count+=1
        idx+=move
        move = lst[idx]
        if lst[idx] >= 3:
            lst[idx] = lst[idx]-1
        else:
            lst[idx] = int(lst[idx])+1
    return count

def get_lst(fd):
    lst = []
    for line in fd:
        line = line.strip()
        lst = lst + [int(line)]
    return lst

fd = open("help.txt")
lst = get_lst(fd)
print(lst)
print(move(lst))
