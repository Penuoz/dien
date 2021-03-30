neg, pos = 0, 0

with open(r'D:\DATA\tianmao\local_test') as fp:
    for line in fp.readlines():
        items = line.strip('\n').split('\t')
        if items[0] == '0':
            neg += 1
        else:
            pos +=1
print(neg, pos)