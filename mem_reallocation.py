

def move(lst):
    large = lst[0]
    large_idx = 0
    for e in range(0,len(lst)):
        if lst[e] > large:
            large = lst[e]
            large_idx = e
    print(large)
    print(large_idx)
    lst[large_idx] = 0
    while large >0:
        if large_idx + 1 >= len(lst):
            large_idx = 0
        else:
            large_idx +=1
        
        lst[large_idx] +=1
        large -=1
    return lst

            



def check_arrange(lst,dic):
    st = ""
    for e in lst:
        st += str(e)
        st += ","
    if st in dic:
        return False
    else:
        dic[st] = 1
    return dic

def check_arrange2(lst,st):
    st2 = ""
    for e in lst:
        st2 += str(e)
        st2 += ","
    print("st2 is ",st2)
    print("st is ",st)
    if st2 == st:
        return False
    return True



def get_input(fd):
    st = fd.readline()
    lst = []
    st = st.strip()
    st = st.split("\t")
    for c in st:
        c = int(c)
        lst.append(c)
    return lst





def main():
    fd = open("help.txt")
    lst = get_input(fd)
    count = 0
    dic = {}
    dic = check_arrange(lst,dic)
    while dic != False:
        print("count ",count)
        move(lst)
        print(lst)
        count +=1
        dic = check_arrange(lst,dic)
        print(dic)
    print(count)
    dic = True
    st = "1,0,14,14,12,12,10,10,8,8,6,6,4,3,2,1,"
    count = 0
    while dic != False:
        print("count ",count)
        move(lst)
        print(lst)
        count +=1
        dic = check_arrange2(lst,st)
        print(dic)
    print(count)



main()
    
