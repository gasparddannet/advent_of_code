import timeit

# file = "example"
file = "input"

##############
### Part 1 ###
##############

def show_diagram(diagram):
    print("############################")
    for line in diagram:
        string_line = ''.join(line)
        print(string_line)
    print("############################")

start = timeit.default_timer()

diagram = []
with open(file,"r") as file:
    for line in file:
        line = line.strip()
        # print("line:",line)
        l = list(line)
        # print("l:",l)
        diagram.append(l)

def get_nb_adjacent_rolls(diagram,i,j,n,m):
    nb_adjacent_rolls = 0
    if i-1 >=0:
        if diagram[i-1][j]=='@':
            nb_adjacent_rolls+=1
        if j-1>=0:
            if diagram[i-1][j-1]=='@':
                nb_adjacent_rolls+=1
        if j+1<m:
            if diagram[i-1][j+1]=='@':
                nb_adjacent_rolls+=1
    if j-1>=0:
        if diagram[i][j-1]=='@':
            nb_adjacent_rolls+=1
    if j+1<m:
        if diagram[i][j+1]=='@':
            nb_adjacent_rolls+=1    
    if i+1 < n:
        if diagram[i+1][j]=='@':
            nb_adjacent_rolls+=1
        if j-1>=0:
            if diagram[i+1][j-1]=='@':
                nb_adjacent_rolls+=1
        if j+1<m:
            if diagram[i+1][j+1]=='@':
                nb_adjacent_rolls+=1
    return nb_adjacent_rolls

n = len(diagram)
m = len(diagram[0])
res = 0
pos = []
new_diagram = [['0' for _ in range(m)] for _ in range(n)]
# show_diagram(new_diagram)

for i in range(n):
    for j in range(m):
        new_diagram[i][j] = diagram[i][j]

        if diagram[i][j]=='@':
            nb_adjacent_rolls = get_nb_adjacent_rolls(diagram,i,j,n,m)
            if nb_adjacent_rolls < 4:
                res+=1
                pos.append((i,j))
                new_diagram[i][j] = 'x'
                # diagram[i][j]='x'

show_diagram(diagram)
show_diagram(new_diagram)

stop = timeit.default_timer()
time = stop-start
print(f"time: {time:4f}s")
print("result:",res)
# print("pos:",pos)