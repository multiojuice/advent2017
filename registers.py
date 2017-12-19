



def get_info():
    fd = open("help.txt")
    dic = {}
    for line in fd:
        line = line.split()
        if line[0] in dic:
            pass
        else:
            dic[line[0]] = 0
    print(dic)   
    fd.close()
    return dic



def interpret(dic):
    fd = open("help.txt")
    maxNum = 0
    for line in fd:
        lst = []
        line = line.strip()
        line = line.split()
        statement = "dic['"+line[4]+"']"+line[5]+line[6]
        print(statement)
        if eval(statement):
            if line[1] == "inc":
                dic[line[0]] += int(line[2])
            elif line[1] == "dec":
                dic[line[0]] -= int(line[2])

            if dic[line[4]] >= maxNum:
                maxNum = dic[line[4]]
    print(dic)
    high = 0
    for val in dic.values():
        if val >high:
            high = val
    
    print(high)
    fd.close()
    return maxNum
     






dic = get_info()


