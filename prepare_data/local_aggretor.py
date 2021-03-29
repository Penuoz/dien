import sys
import hashlib
import random
import os
from sklearn.model_selection import train_test_split
import collections

root_path = r'D:\DATA\tianmao'
fin = open(os.path.join(root_path, "jointed-new"), "r")
ftrain = open(os.path.join(root_path, "local_train"), "w")
ftest = open(os.path.join(root_path, "local_test"), "w")

uid_sid_pos = collections.defaultdict(list)
uid_sid_neg = collections.defaultdict(list)
for line in fin:
    items = line.strip().split("\t")
    token = items[1] + '_' + items[2]
    if items[0] == '0':
        uid_sid_neg[token].append(line)
    else:
        uid_sid_pos[token].append(line)

X = list(uid_sid_neg.keys()) + list(uid_sid_pos.keys())
y = [0] * len(uid_sid_neg) + [1] * len(uid_sid_pos)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

last_user = "0"
last_seller = "0"
common_fea = ""
line_idx = 0
for key in x_train:
    if key in uid_sid_pos:
        lines = uid_sid_pos[key]
    else:
        lines = uid_sid_neg[key]
    item_id_list = []
    cat_list = []
    for line in lines:
        items = line.strip().split("\t") # label, user, seller, item, cat, rate, time
        clk = items[0]
        user = items[1]
        seller = items[2]
        item = items[3]
        cat = items[4]
        rate = items[5]
        time = items[6]

        item_id_list.append(item)
        cat_list.append(cat)
    cat_str = ""
    iid_str = ""
    for c1 in cat_list:
        cat_str += c1 + ""
    for mid in item_id_list:
        iid_str += mid + ""
    ftrain.write(clk + "\t" + user + "\t" + seller +"\t" + iid_str + "\t" + cat_str + '\n')

last_user = "0"
last_seller = "0"
common_fea = ""
line_idx = 0
for key in x_test:
    if key in uid_sid_pos:
        lines = uid_sid_pos[key]
    else:
        lines = uid_sid_neg[key]
    item_id_list = []
    cat_list = []
    for line in lines:
        items = line.strip().split("\t") # label, user, seller, item, cat, rate, time
        clk = items[0]
        user = items[1]
        seller = items[2]
        item = items[3]
        cat = items[4]
        rate = items[5]
        time = items[6]

        item_id_list.append(item)
        cat_list.append(cat)
    cat_str = ""
    iid_str = ""
    for c1 in cat_list:
        cat_str += c1 + ""
    for mid in item_id_list:
        iid_str += mid + ""
    ftest.write(clk + "\t" + user + "\t" + seller +"\t" + iid_str + "\t" + cat_str + '\n')