import timeit

file = "example"
# file = "input"

##############
### Part 1 ###
##############

start = timeit.default_timer()


def get_max_list_not_in_index(l, list_index):
    # i, m = max(enumerate(l), key=lambda x:(int(x[1]) if x[0] not in list_index else 0))
    i, m = -1,-1
    if len(list_index)>0:
        min_index = min(list_index)
    for k in range(len(l)-1,-1,-1):
        v = int(l[k])
        if len(list_index) == 0:
            if v>m:
                i, m = k, v
        else:
            if k not in list_index:
                if v >= m and k>i:
                    i, m = k, v
                if k>min_index:
                    i, m= k, v
    
    return i, m

res = 0
with open(file,"r") as file:
    for line in file:
        line = line.strip()
        l = list(line)
        list_index = []
        print("l:",l)
        for _ in range(12):
            i,m = get_max_list_not_in_index(l, list_index)
            print("m:",m)
            print("i:",i)
            list_index.append(i)
            print("list_index:",list_index)
        list_index.sort()
        print("list_index:",list_index)
        temp=""
        for i in list_index:
            temp+=l[i]
        print("temp:",temp)
        res += int(temp)

stop = timeit.default_timer()
time = stop-start
print(f"time: {time:4f}s")
print("result:",res)
