import collections

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

temp = temp.replace("% ", "")
temp = temp.split(" ")
m = int(temp[1])
n = int(temp[2])

mat = [[0] * n for _ in range(m)]

for i in pointer_list:
    mat[int(i[0]) - 1][int(i[1]) - 1] = 1

ta_count = 0
tb_count = 0
tc_count = 0
td_count = 0


def counter(i, j_lis):
    global ta_count
    global tb_count
    global tc_count
    global td_count
    for j1 in j_lis:
        for a in range(n):
            if mat[j1][a] == 1 and mat[a][i] == 1 and mat[i][a] == 0:
                #print(i+1, j1+1, a+1)
                ta_count += 1
            if mat[j1][a] == 1 and mat[a][i] == 1 and mat[i][a] == 1:
                #print(i+1, j1+1, a+1)
                tc_count += 1
            if mat[j1][a] == 1 and mat[a][i] == 0 and mat[i][a] == 1:
                tb_count += 1
            if mat[j1][a] == 1 and mat[a][i] == 0 and mat[i][a] == 0:
                td_count += 1


for i in range(m):
    j_list = []
    for j in range(n):
        if mat[i][j] == 1:
            j_list += j,
    counter(i, j_list)

print(ta_count, tb_count, tc_count, td_count)


