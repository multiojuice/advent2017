"""
Owen Sullivan
"""


def knot(lst):
    fd = open("help.txt")
    data = fd.readline()
    data = data.split(',')
    jump = 0 
    idx = 3
    for e in data:
        print("current string: ",lst)
        e = int(e)
        if e == 1:
            pass
        elif idx+e > len(lst)-1:
            print("here1")
            diff = idx+e-len(lst)-1
            new_lst = lst[idx:] + lst[:diff+1]
            print("new",new_lst)
            new_lst = new_lst[::-1]
            print("reverse",new_lst)
            front = new_lst[:diff+1]
            print("front",front)
            end = new_lst[len(lst)-idx:]
            print("end",end)
            lst = end + lst[diff+1:idx] + front

        else:
            print("here2")
            new_lst = lst[idx:idx+e]
            new_lst = new_lst[::-1]
            lst = lst[:idx] + new_lst + lst[idx+e:]
        
        jump+=1 
        if idx + e + jump >= len(lst):
            idx = idx + e + jump - len(lst)-1
        else:
            idx = idx + e + jump
        
    print(lst)
    return lst[0] * lst[1]

    
lst = []
for i in range(0,256):
    lst.append(i)
print(i)
t = [4,3,0,1,2]
print(knot(t))





