

def read_through():
    fd = open("help.txt")
    data = fd.readline()
    total = 0
    previous = 0
    garbage = False
    idx = 0
    count = 0
    while idx <len(data):
        print("char",data[idx])
        if data[idx] == "!":
            idx+=1
        elif garbage == False:
            if data[idx] == "{":
                previous+=1
                total+=previous
            elif data[idx] == "}":
                previous -= 1
            elif data[idx] == "<":
                garbage = True
                print("Here bitch")
            else:
                pass
        elif garbage == True:
                if data[idx] == ">":
                    garbage = False
                else:
                    count += 1
        idx+=1
        print(garbage)
        print("idx",idx)
        print("prev",previous)
        print("total",total)
    print(total)
    print(count)

read_through()






