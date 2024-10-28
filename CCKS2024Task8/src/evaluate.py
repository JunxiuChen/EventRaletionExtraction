# 根据提交结果计算f1分数
# 本次任务采用精确率（Precision, P）、召回率（Recall, R）、F1值（F1-measure, F1）来评估事件关系抽取效果。使用F1作为最终评价指标。
# 事件关系抽取精确率=识别出的真实事件关系数量/识别出的事件关系总数量
# 事件关系抽取召回率=识别出的真实事件关系数量/标注的事件关系总数量
# 事件关系抽取F1值=(2*事件关系抽取精确率*事件关系抽取召回率)/(事件关系抽取精确率+事件关系抽取召回率)
from src.utils import *
testa_gt = load_line_data('../data/比赛数据-无GT/有GT的测试数据/testa_gt.json')
result = load_line_data('../output/submit.txt')

annotated_relation_num = 0
identified_relation_num = 0
TP = 0

for i in range(len(testa_gt)):
    annotated_relation_num += len(testa_gt[i]["relations"])
    identified_relation_num += len(result[i]["relations"])
    gt_list = []
    for j in testa_gt[i]["relations"]:
        pair_dict = {}
        pair_dict["one_event_id"] = j["one_event"]["id"]
        pair_dict["other_event_id"] = j["other_event"]["id"]
        pair_dict["relation_type"] = j["relation_type"]
        gt_list.append(pair_dict)

    for k in result[i]["relations"]:
        if k in gt_list:
            TP += 1
            gt_list.remove(k)


P = TP/identified_relation_num
R = TP/annotated_relation_num
F1 = (2*P*R)/(P+R)
print(P, R, F1)
print(identified_relation_num, annotated_relation_num)
print(TP)



