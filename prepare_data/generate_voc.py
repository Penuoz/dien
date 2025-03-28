import _pickle as cPickle
import os

root_path = r'D:\DATA\tianmao'
f_train = open(os.path.join(root_path, "local_train_splitByUser"), "r")
uid_dict = {}
mid_dict = {}
cat_dict = {}

iddd = 0
for line in f_train:
    arr = line.strip("\n").split("\t")
    clk = arr[0]
    uid = arr[1]
    mid = arr[2]
    cat = arr[3]
    mid_list = arr[4]
    cat_list = arr[5]
    if uid not in uid_dict:
        uid_dict[uid] = 0
    uid_dict[uid] += 1
    if mid not in mid_dict:
        mid_dict[mid] = 0
    mid_dict[mid] += 1
    if cat not in cat_dict:
        cat_dict[cat] = 0
    cat_dict[cat] += 1
    if len(mid_list) == 0:
        continue
    for m in mid_list.split(""):
        if m not in mid_dict:
            mid_dict[m] = 0
        mid_dict[m] += 1
    #print iddd
    iddd+=1
    for c in cat_list.split(""):
        if c not in cat_dict:
            cat_dict[c] = 0
        cat_dict[c] += 1

sorted_uid_dict = sorted(uid_dict.items(), key=lambda x:x[1], reverse=True)
sorted_mid_dict = sorted(mid_dict.items(), key=lambda x:x[1], reverse=True)
sorted_cat_dict = sorted(cat_dict.items(), key=lambda x:x[1], reverse=True)

uid_voc = {}
index = 0
for key, value in sorted_uid_dict:
    uid_voc[key] = index
    index += 1

mid_voc = {}
mid_voc["default_mid"] = 0
index = 1
for key, value in sorted_mid_dict:
    mid_voc[key] = index
    index += 1

cat_voc = {}
cat_voc["default_cat"] = 0
index = 1
for key, value in sorted_cat_dict:
    cat_voc[key] = index
    index += 1

# with open(os.path.join(root_path, "uid_voc.pkl"), "wb") as fp:
#     cPickle.dump(uid_voc, fp)
cPickle.dump(mid_voc, open(os.path.join(root_path, "mid_voc.pkl"), "wb"))
cPickle.dump(cat_voc, open(os.path.join(root_path, "cat_voc.pkl"), "wb"))
