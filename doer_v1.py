import collections

#similar technique but instead we use a dictionary to store node relations
#we dont waste memory for storing no relations
#its still slow though

file = open("out.convote", "r")
i = 0
temp = ''
pointer_list = []
for line in file:
    if i == 1:
        temp = str(line)
    elif i >= 2:
        pointer_list += str(line).split(" ")[:2],
    i += 1

# temp = temp.replace("% ", "")
# temp = temp.split(" ")
# m = int(temp[1])
# n = int(temp[2])


dic = collections.defaultdict(set)

for i in pointer_list:
    dic[int(i[0])].add(int(i[1]))
    if int(i[1]) not in dic:
        dic[int(i[1])] = set()

ta_count = 0
tb_count = 0
tc_count = 0
td_count = 0

for i in dic:
    for j in dic[i]:
        if j in dic and i not in dic[j]:
            for k in dic[j]:
                if k in dic and i in dic[k] and k not in dic[i] and j not in dic[k]:
                    ta_count += 1
                if k in dic and i in dic[k] and k in dic[i] and j not in dic[k]:
                    tc_count += 1
                if k in dic:
                    if i not in dic[k] and k in dic[i] and j not in dic[k]:
                        tb_count += 1
                elif k not in dic:
                    if k in dic[i] and j not in dic[k]:
                        tb_count += 1
                if k in dic and i not in dic[k] and k not in dic[i] and j not in dic[k]:
                    td_count += 1
                elif k not in dic and k not in dic[i] and j not in dic[k]:
                    td_count += 1


print(ta_count, tb_count, tc_count, td_count)

#stack_overflow = 1286 79334 50 10185002
#flickr_growth = 282201198 868926209 1561217553 16942301238
#out.moreno_rhesus_rhesus = 0 2 7 11
