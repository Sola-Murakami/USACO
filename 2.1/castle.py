"""
ID: 
LANG: PYTHON3
TASK: castle
"""
def num_to_walls(num):
    # input is num as a base 10 int or maybe string
    # output is a tuple (1, 0, 1, 1) for walls (W, N, E, S)

    num = int(num)
    tup = []

    for _ in range(4):
        tup.append(num % 2)
        num //= 2
    
    return tuple(tup)

with open('castle.in') as f:
    x, y = map(int, f.readline().strip().split())

    # input is (row, column) 0-indexed
    # output is walls
    d = {}

    for idx in range(y):
        st = f.readline().strip()

        for idx2, num in enumerate(st.split()):
            num = int(num)
            d[(idx, idx2)] = num_to_walls(num)

node_list = list(d)
island_list = []

while len(node_list) > 0:
    node = node_list.pop()
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    bfs = [node]
    island = {node}

    while len(bfs) > 0:
        n = bfs.pop()
        walls = d[n]
        
        for i in range(len(walls)):
            if not walls[i]:
                dired = dirs[i]
                temp_y = n[0] + dired[0]
                temp_x = n[1] + dired[1]
                if 0 <= temp_y < y and 0 <= temp_x < x:
                    if (temp_y, temp_x) not in island:
                        node_list.remove((temp_y, temp_x))
                        island.add((temp_y, temp_x))
                        bfs.append((temp_y, temp_x))
        
    island_list.append(list(island))

# input is node (row, column)
# output is island index 0, 1, 2 from island list
island_dict = {}
for i in range(len(island_list)):
    for n in island_list[i]:
        island_dict[n] = i

island_len = {}
dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
sigs = ['W', 'N', 'E', 'S']

for i in range(len(island_list)):
    island_len[i] = len(island_list[i])

print(island_dict, island_len)

max_room = 0
break_pos = None
break_dir = ''
for j in range(x):
    for i in range(y - 1, -1, -1):
        n = (i, j)
        isl = island_dict[n]
        walls = d[n]

        for pos in range(4):
            if walls[pos]:
                dired = dirs[pos]
                temp_y = n[0] + dired[0]
                temp_x = n[1] + dired[1]
                temp_n = (temp_y, temp_x)

                if 0 <= temp_y < y and 0 <= temp_x < x:
                    temp_isl = island_dict[temp_n]
                    if isl != temp_isl:
                        new_room = island_len[isl] + island_len[temp_isl]
                        
                        if new_room > max_room:
                            max_room = new_room
                            break_dir = sigs[pos]
                            break_pos = f'{n[0]+1} {n[1]+1}'

with open('castle.out', 'w') as f:
    mx = 0
    for stst in island_list:
        mx = max(len(stst), mx)
    
    f.write(f'{len(island_list)}\n{mx}\n{max_room}\n{break_pos} {break_dir}\n')
    

