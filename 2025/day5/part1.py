import timeit

# file = "example"
file = "input"

start = timeit.default_timer()

list_fresh = []
list_ingredient = []
with open(file,"r") as file:
    for line in file:
        line = line.strip()
        # print("line:",line)
        if '-' in line:
            line = line.split('-')
            id1 = int(line[0])
            id2 = int(line[1])
            list_fresh.append((id1,id2))
        else:
            if len(line)>0:
                id = int(line)
                list_ingredient.append(id)

print("list_fres:",list_fresh)
print("list_ingredient:",list_ingredient)

res = 0
for id in list_ingredient:
    for (idf1,idf2) in list_fresh:
        if idf1 <= id <= idf2:
            # print("id:",id)
            res+=1
            break

stop = timeit.default_timer()
time = stop-start
print(f"time: {time:4f}s")
print("result:",res)