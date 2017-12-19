"""
Author- Owen Sullivan
"""

def make_sense_of_this_input_please():
    fd = open("help.txt")
    data = []
    count = 0
    for line in fd:
        dic = {}
        line = line.split()
        for e in range(2,len(line)):
            if line[e][len(line[e])-1] == ",":
                dic[line[e][:-1]] = 0
            else:
                dic[line[e]] = 0
        data.append(dic)
    return data



def make_sense_of_this_data_please(data):
     counted = make_recur(data[0],data,{},0)
     groups = 1
     for i in range(0,2000):
         if str(i) in counted:
             pass
         else:
             print("index is",i)
             counted = make_recur(data[i],data,counted,0)
             groups+=1
     return groups
    

def make_recur(dic,data,counted,count):
    
    for key in dic.keys():
        print("key is ",key)
        if key in counted:
            pass
        else:
            print("count =",count)
            counted[key] = 0
            counted = make_recur(data[int(key)],data,counted,count)
            #count +=1
    return counted




data = make_sense_of_this_input_please()
print(data)
print(len(data))

groups = make_sense_of_this_data_please(data)

print(groups)





