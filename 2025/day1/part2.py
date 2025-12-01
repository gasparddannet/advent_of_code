# file = "example"
file = "input"

##############
### Part 2 ###
##############
pos = 50
cpt0 = 0
with open(file,"r") as file:
    for line in file:
        line = line.strip()
        # print("line;",line)
        dir = line[0]
        dir = 1 if line[0]=="R" else -1
        num = int(line[1:])
        previous_pos = pos

        pos += (dir * num)
        q = pos//100
        pos = pos%100
        print(f"dir:{dir}, num:{num}\told_pos:{previous_pos}, q:{q}, pos:{pos}")
        if previous_pos == 0:
            if q<0:
                q+=1

        cpt0 += abs(q)
        if pos==0 and previous_pos!=0 and pos<previous_pos and q<=0:
            cpt0+=1
        
        print(f"cpt0:{cpt0}")
print("cpt0:",cpt0)

