import timeit

# file = "example"
file = "input"

##############
### Part 1 ###
##############

start = timeit.default_timer()

res = 0
with open(file,"r") as file:
    for line in file:
        line = line.strip()
        # print("line:",line)
        l = list(line)
        # print("l:",l)
        m = max(l)
        # print("m:",m)
        i = l.index(m)
        # print("i:",i)
        if i == len(l)-1:
            m2=m
            m1 = max(l[:i])
        else:
            m1 = m
            m2 = max(l[i+1:])
        # print("m1:",m1)
        # print("m2:",m2)
        temp = m1+m2
        # print("temp:",temp)
        res += int(temp)

stop = timeit.default_timer()
time = stop-start
print(f"time: {time:4f}s")
print("result:",res)
