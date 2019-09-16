import collections
from datetime import datetime

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


for a, b in pointer_list:
    a_outs = dic[a]
    if b in dic and b in a_outs:
        b_outs = dic[b]
        if a not in b_outs:
            for pc in b_outs:
                if pc in dic:
                    pc_outs = dic[pc]
                    if b not in pc_outs:
                        if a in pc_outs and pc in a_outs:
                            tc_count += 1
                        elif a in pc_outs and pc not in a_outs:
                            ta_count += 1
                        elif a not in pc_outs and pc in a_outs:
                            tb_count += 1
                        else:
                            td_count += 1
                else:
                    if pc in a_outs:
                        tb_count += 1
                    else:
                        td_count += 1


print(ta_count, tb_count, tc_count, td_count)
end = datetime.now() - start
print("Time took -> ", end.total_seconds())