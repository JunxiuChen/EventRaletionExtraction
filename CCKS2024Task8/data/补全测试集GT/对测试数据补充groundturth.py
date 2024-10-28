from src.utils import *


ori_train_data = load_line_data("../DEIE/train.json")
# ori_test_data = load_line_data("../DEIE/test.json")
# ori_dev_data = load_line_data("../DEIE/dev.json")
testa = load_line_data("testa.json")
testb = load_line_data("testb.json")


def get_id2relations(ori_train_data):
    id2relations = {}
    for line in ori_train_data:
        news_id = line["news-ID"]
        relations = line["relations"]
        id2relations[news_id] = relations
    return id2relations


def save_gt_test_data(test_data_without_gt, save_path, id2relations):
    test_gt = []
    count = 0
    for line in test_data_without_gt:
        new_id = line["new-ID"]
        if new_id in id2relations.keys():
            line["relations"] = id2relations[new_id]
            test_gt.append(line)
        else:
            count += 1
    print("在全量训练数据中没有GT的测试数据数量：", count)
    save_data_bylines(test_data_without_gt, save_path)
    print("保存完成，保存路径：", save_path)


id2relations = get_id2relations(ori_train_data)
# save_gt_test_data(testa, './有GT的测试数据/testa_with_gt.json', id2relations)
# save_gt_test_data(testb, './有GT的测试数据/testb_with_gt.json', id2relations)


# 只保存对应测试数据的GT便于计算分数
def save_gt(test_data_without_gt, save_path, id2relations):
    gt = []
    count = 0
    for line in test_data_without_gt:
        new_id = line["new-ID"]
        temp_dic = {}
        if new_id in id2relations.keys():
            temp_dic["relations"] = id2relations[new_id]
            gt.append(temp_dic)
        else:
            count += 1
    save_data_bylines(gt, save_path)


# save_gt(testa, './有GT的测试数据/testa_gt.json', id2relations)
# save_gt(testb, './有GT的测试数据/testb_gt.json', id2relations)




