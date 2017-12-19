"""
Owen Sullivan
"""
def dance(lst):
    fd = open("help.txt")
    data = fd.readline()
    data = data.split(",")
    for e in data:
        if e[0] == 'x':
            place1 = 0
            place2 = 0
            if e[2] == "/":
                place1 = int(e[1])
                place2 = int(e[3:])
            else:
                place1 = int(e[1]+e[2])
                place2 = int(e[4:])
            temp = lst[place1]
            lst[place1] = lst[place2]
            lst[place2] = temp
        elif e[0] == 'p':
            content1 = e[1]
            content2 = e[3]
            place1 = 0
            place2 = 0
            for idx in range(0,len(lst)):
                if lst[idx] == content1:
                    place1 = idx
                if lst[idx] == content2:
                    place2 = idx
            lst[place1] = content2
            lst[place2] = content1
        elif e[0] == 's':
            idx = int(e[1:])
            lst = lst[-idx:] + lst[:-idx]
    return lst
            


st = "abcdefghijklmnop"
lst = []
lst1 = []
for c in st:
    lst.append(c)
    lst1.append(c)
print(lst)
for i in range(0,40):
    print(i)
    lst = dance(lst)
    if lst == lst1:
        break
print(lst)






