# file = "example"
file = "input"

##############
### Part 1 ###
##############
pos = 50
cpt0 = 0
with open(file,"r") as file:
    for line in file:
        line = line.strip()
        # print("line;",line)
        dir = line[0]
        dir = 1 if line[0]=="R" else -1
        # print("dir:",dir)
        num = int(line[1:])
        # print("num:",num)
        pos += (dir * num)
        pos = pos%100
        # print("pos:",pos)
        if pos==0:
            cpt0 += 1

print("cpt0:",cpt0)

