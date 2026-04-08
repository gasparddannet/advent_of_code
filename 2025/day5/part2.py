import timeit

# file = "example"
# file = "example2"
file = "input"

start = timeit.default_timer()

list_fresh = []
with open(file,"r") as file:
    for line in file:
        line = line.strip()
        # print("line:",line)
        if '-' in line:
            line = line.split('-')
            id1 = int(line[0])
            id2 = int(line[1])
            list_fresh.append((id1,id2))

print("list_fres:",list_fresh)

new_list_fresh = []
new_list_fresh.append(list_fresh[0])
for i in range(1,len(list_fresh)):
    idf1, idf2 = list_fresh[i]

    for j in range(0,i):
        tempid1, tempid2 = list_fresh[j]
        if tempid1 <= idf1 <= tempid2:
            idf1 = tempid2+1
        if tempid1 <= idf2 <= tempid2:
            idf2 = tempid1-1
    new_list_fresh.append((idf1,idf2))

print("new_list_fres:",new_list_fresh)

res = 0
for (id1, id2) in new_list_fresh:
    if id2>id1:
        res += id2-id1+1

stop = timeit.default_timer()
time = stop-start
print(f"time: {time:4f}s")
print("result:",res)