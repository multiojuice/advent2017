


def first_search():
    fd = open("help.txt")
    
    for line in fd:
        line = line.split()
        if len(line) > 3:
            st = ""
            for e in line:
                st +=e
                st += " "
            print(st)



def second_search():
    fd = open("help2.txt")
    dic = {}
    for line in fd:
        line = line.strip()
        line = line.split()
        for e in range(3,len(line)):
            if line[e] in dic:
                pass
            else:
                if line[e][len(line[e])-1] != ",":
                    dic[line[e]] = 1
                else:
                    dic[line[e][:-1]] = 1
    fd.close()
    fd = open("help2.txt")
    for line in fd:
        line = line.strip()
        line = line.split()
        if line[0] in dic:
            pass
        else:
            print("answer",line[0])
    

second_search()
