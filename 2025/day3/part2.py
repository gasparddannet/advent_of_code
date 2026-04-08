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
        l_og = l.copy()
        list_index = []

        l = list(enumerate(l))
        l_enum_og = l.copy()
        print("l:",l)

        for k in range(12):
            # i,m = get_max_list_not_in_index(l, list_index)


            i_og, m = max(l, key=lambda x:(int(x[1]) if x[0] not in list_index else 0))
            list_index.append(i_og)
            i = l.index((i_og,m))

            if i == len(l)-1:
                l = l[:i]
            else:
                min_index = min(list_index)
                if len(l[min_index+1:]) >= 11-k:
                    l = l[min_index+1:]
                else:
                    l = l_enum_og.copy()
                    l = l[min_index:]

            print("m:",m)
            print("i_og:",i_og)
            print("list_index:",list_index)
            print("l:",l)
        list_index.sort()
        print("list_index:",list_index)
        temp=""
        for i in list_index:
            temp+=l_og[i]
        print("temp:",temp)
        res += int(temp)

stop = timeit.default_timer()
time = stop-start
print(f"time: {time:4f}s")
print("result:",res)
