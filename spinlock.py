




def move(val):
    lst = [0]
    count = 0
    num = 1
    idx = 0
    while num <=50000000:
        if count != val:
            count +=1
            idx +=1
            if idx >= len(lst):
                idx = idx-len(lst)
        else:
            lst = lst[:idx] + [num] + lst[idx:]
            num +=1
            idx +=1
            count = 0
            
    count = 0

    while True:
        if lst[count] == 0:
            break
        count +=1
    print(lst[count+1])


move(377)
        
        





