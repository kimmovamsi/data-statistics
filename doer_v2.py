import collections
from datetime import datetime

#similar technique but instead we use a dictionary to store node relations
#we dont waste memory for storing node relations
#its still slow though
#dictionary traversal method

start = datetime.now()

file = open("out.stackexchange-stackoverflow", "r")
i = 0
temp = ''
pointer_list = []
dic = collections.defaultdict(set)
for line in file:
    if i == 1:
        temp = str(line)
    elif i >= 2:
        [a, b] = str(line).split(" ")[:2]
        a, b = int(a), int(b)
        dic[a].add(b)
        if b not in dic:
            dic[b] = set()
        pointer_list += [a, b],
    i += 1

ta_count = 0
tb_count = 0
tc_count = 0
td_count = 0

for i in dic:
    for j in dic[i]:
        if i not in dic[j]:
            for k in dic[j]:
                if k in dic and j not in dic[k]:
                    if k not in dic[i] and i in dic[k]:
                        ta_count += 1
                    elif k in dic[i] and i not in dic[k]:
                        tb_count += 1
                    elif k in dic[i] and i in dic[k]:
                        tc_count += 1
                    else:
                        td_count += 1
                elif k not in dic:
                    if k in dic[i]:
                        tb_count += 1
                    else:
                        td_count += 1


print(ta_count, tb_count, tc_count, td_count)
end = datetime.now() - start
print("Time took -> ", end.total_seconds())
