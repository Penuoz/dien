import pandas as pd
import os
import random

root_path = r'D:\DATA\tianmao'
# file = pd.read_csv(r'D:\DATA\tianmao\user_log_format1.csv', dtype=str)
# with open(os.path.join(root_path, 'item-info'), 'w') as fp1:
#     with open(os.path.join(root_path, 'reviews-info'), 'w') as fp2:
#         for idx, row in file.iterrows():
#             item, cat, seller, time, rate, user = str(row['item_id']), str(row['cat_id']), str(row['seller_id']), \
#                                             str(row['time_stamp']), str(row['action_type']), str(row['user_id'])
#             if rate == '0':
#                 rate = 1
#             elif rate == '1':
#                 rate = 2
#             elif rate == '2':
#                 rate = 3
#             elif rate == '3':
#                 rate = 2
#             fp1.write("{}\t{}\t{}\n".format(item, cat, seller))
#             fp2.write("{}\t{}\t{}\t{}\n".format(user, item, rate, time))

def manual_join():
    f_rev = open(os.path.join(root_path, "reviews-info"), "r")
    user_map = {} # 用户id [("用户id 商品id 商品评分 评价时间", 评价时间)]
    item_list = [] # 商品id
    for line in f_rev:
        line = line.strip()
        items = line.split("\t")
        #loctime = time.localtime(float(items[-1]))
        #items[-1] = time.strftime('%Y-%m-%d', loctime)
        if items[0] not in user_map:
            user_map[items[0]]= []
        user_map[items[0]].append(("\t".join(items), float(items[-1])))
        item_list.append(items[1])
    f_meta = open(os.path.join(root_path, "item-info"), "r")
    meta_map = {}
    for line in f_meta:
        arr = line.strip().split("\t")
        if arr[0] not in meta_map:
            meta_map[arr[0]] = arr[1]
            arr = line.strip().split("\t")
    fo = open(os.path.join(root_path, "jointed-new"), "w")
    for key in user_map:
        sorted_user_bh = sorted(user_map[key], key=lambda x:x[1]) # 按照评论时间排序
        for line, t in sorted_user_bh:
            items = line.split("\t") # "用户id 商品id 商品评分 评价时间"
            asin = items[1]
            j = 0
            while True:
                asin_neg_index = random.randint(0, len(item_list) - 1)
                asin_neg = item_list[asin_neg_index] # 随机选择一个商品id
                if asin_neg == asin:
                    continue
                items[1] = asin_neg
                fo.write("0" + "\t" + "\t".join(items) + "\t" + meta_map[asin_neg] + '\n')
                j += 1
                if j == 1:             #negative sampling frequency
                    break
            if asin in meta_map:
                fo.write("1" + "\t" + line + "\t" + meta_map[asin] + '\n')
            else:
                fo.write("1" + "\t" + line + "\t" + "default_cat" + '\n')


def split_test():
    fi = open(os.path.join(root_path, "jointed-new"), "r")
    fo = open(os.path.join(root_path, "jointed-new-split-info"), "w")
    user_count = {} # 用户id 出现次数
    for line in fi:
        line = line.strip()
        user = line.split("\t")[1]
        if user not in user_count:
            user_count[user] = 0
        user_count[user] += 1
    fi.seek(0)
    i = 0
    last_user = "A26ZDKC53OP6JD"
    for line in fi:
        line = line.strip()
        user = line.split("\t")[1]
        if user == last_user:
            if i < user_count[user] - 2:  # 1 + negative samples
                fo.write("20180118" + "\t" + line + '\n')
            else:
                fo.write("20190119" + "\t" + line + '\n')
        else:
            last_user = user
            i = 0
            if i < user_count[user] - 2:
                fo.write("20180118" + "\t" + line + '\n')
            else:
                fo.write("20190119" + "\t" + line + '\n')
        i += 1

# manual_join()
split_test()
