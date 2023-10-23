tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

width_list = [0] * len(tableData)
# print(width_list)
# new_table = [0] * len(tableData[0]) --> reference issue: when width_list change,  new_table change accordingly
new_table = []
for i in range(len(tableData[0])):
    new_table.append([0] * len(tableData))
# print(new_table)

for i in range(len(tableData)):
    max_width = 0
    for j in range(len(tableData[i])):
        new_table[j][i] = tableData[i][j]
        # print(new_table)
        if max_width <= len(tableData[i][j]):
            max_width = len(tableData[i][j])
        
        if j == len(tableData[i]) - 1:
            width_list[i] = max_width
            # print(width_list)

# print(new_table)

for c1, v1 in enumerate(new_table):
    new_line = ''
    # print(v1)
    for c2, v2 in enumerate(v1):
        # print(v2)
        new_line = new_line + v2.rjust(width_list[c2]) + ' '
        if c2 == len(v1) - 1:
            print(new_line)

