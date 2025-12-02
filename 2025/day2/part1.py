import timeit

# file = "example"
file = "input"

##############
### Part 1 ###
##############

def get_invalid_ids(first_id, last_id):
    sum_inv_ids = 0
    for i in range(int(first_id), int(last_id)+1):
        i = str(i)
        # print("len(i):",len(i))
        if len(i)%2==0 and i[0]!="0":
            m = len(i)//2
            if i[:m] == i[m:]:
                # print("qqqqqqq")
                # print("i:",i)
                sum_inv_ids +=  int(i)
    return sum_inv_ids

start = timeit.default_timer()
inv_ids = 0
with open(file,"r") as file:
    line = file.readline()
    line = line.strip()
    # print("line;",line)
    l = line.split(",")
    print("l:",l)
    for range_id in l:
        s = range_id.split("-")
        first_id = s[0]
        last_id = s[1]
        # print("first_id:",first_id)
        # print("last_id:",last_id)
        inv_ids += get_invalid_ids(first_id, last_id)
        # print()
        
stop = timeit.default_timer()
time = stop-start
print(f"time: {time:4f}s")
print("result:",inv_ids)
