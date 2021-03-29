import pandas as pd
import os
import random
import sys

root_path = r'D:\DATA\tianmao'
file = pd.read_csv(r'D:\DATA\tianmao\user_log_format1.csv', dtype=str)
file1 = pd.read_csv(r'D:\DATA\tianmao\train_format1.csv', dtype=str)
file1.columns = ['user_id', 'seller_id', 'label']
file = pd.merge(file, file1, on=["user_id", 'seller_id'])
# with open(os.path.join(root_path, 'item-info'), 'w') as fp1:
# with open(os.path.join(root_path, 'reviews-info'), 'w') as fp2:
#         for idx, row in file.iterrows():
#             item, cat, seller, time, rate, user, label = str(row['item_id']), str(row['cat_id']), str(row['seller_id']), \
#                                             str(row['time_stamp']), str(row['action_type']), str(row['user_id']), \
#                                                   str(row['label'])
#             if rate == '0':
#                 rate = 1
#             elif rate == '1':
#                 rate = 2
#             elif rate == '2':
#                 rate = 3
#             elif rate == '3':
#                 rate = 2
            # fp1.write("{}\t{}\t{}\n".format(item, cat, seller))
            # fp2.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(label, user, seller, item, cat, rate, time))
            # break

def manual_join():
    f_rev = open(os.path.join(root_path, "reviews-info"), "r")
    user_map = {} # 用户id [("label, user, seller, item, cat, rate, time", 评价时间)]
    item_list = [] # 商品id
    for line in f_rev:
        line = line.strip()
        items = line.split("\t")
        if items[0] not in user_map:
            user_map[items[0]]= []
        user_map[items[0]].append(("\t".join(items), float(items[-1])))
        item_list.append(items[1])
    fo = open(os.path.join(root_path, "jointed-new"), "w")
    for key in user_map:
        sorted_user_bh = sorted(user_map[key], key=lambda x: x[1]) # 按照评论时间排序
        for line, t in sorted_user_bh:
            fo.write(line + '\n')


def split_test():
    fi = open(os.path.join(root_path, "jointed-new"), "r")
    fo = open(os.path.join(root_path, "jointed-new-split-info"), "w")
    user_count = set()
    pos, neg = 0, 0
    for line in fi:
        line = line.strip()
        items = line.split("\t")
        user = items[1]
        seller = items[2]
        if user + '_' + seller not in user_count:
            if line.split("\t")[0] == '0':
                neg += 1
            else:
                pos += 1
            user_count[user] = 0
        user_count[user] += 1

    print(len(user_count))
    print(pos, neg)
    # fi.seek(0)
    # i = 0
    # last_user = "A26ZDKC53OP6JD"
    # for line in fi:
    #     line = line.strip()
    #     user = line.split("\t")[1]
    #     if user == last_user:
    #         if i < user_count[user] - 2:  # 1 + negative samples
    #             fo.write("20180118" + "\t" + line + '\n')
    #         else:
    #             fo.write("20190119" + "\t" + line + '\n')
    #     else:
    #         last_user = user
    #         i = 0
    #         if i < user_count[user] - 2:
    #             fo.write("20180118" + "\t" + line + '\n')
    #         else:
    #             fo.write("20190119" + "\t" + line + '\n')
    #     i += 1

manual_join()
