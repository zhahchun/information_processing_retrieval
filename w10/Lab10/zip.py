import sys

file01 = sys.argv[1]
file02 = sys.argv[2]
file03 = sys.argv[3]
file01_list = []
file02_list = []

with open(file01, 'r') as f01:
    for line in f01:
        file01_list.append(line)

with open(file02, 'r') as f02:
    for line in f02:
        file02_list.append(line)

with open(file03, 'a') as f03:
    for i in range(3):
        print('first file,', file01_list[i], file=f03)
        print('second file,', file02_list[i], file=f03)
