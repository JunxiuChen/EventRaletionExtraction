# 根据提交结果计算f1分数
# 本次任务采用精确率（Precision, P）、召回率（Recall, R）、F1值（F1-measure, F1）来评估事件关系抽取效果。使用F1作为最终评价指标。
# 事件关系抽取精确率=识别出的真实事件关系数量/识别出的事件关系总数量
# 事件关系抽取召回率=识别出的真实事件关系数量/标注的事件关系总数量
# 事件关系抽取F1值=(2*事件关系抽取精确率*事件关系抽取召回率)/(事件关系抽取精确率+事件关系抽取召回率)
import json
def load_line_data(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        line_data = f.readlines()
        for line in line_data:
            dic = json.loads(line)
            data.append(dic)
    return data


gold_result = load_line_data('../CCKS2024Task8/data/补全测试集GT/有GT的测试数据/testb_gt.json')
pred_result = load_line_data('joint/output/42/DEIE/test_prediction.jsonl')

annotated_relation_num = 0
identified_relation_num = 0
TP = 0

for i in range(len(gold_result)):
    annotated_relation_num += len(gold_result[i]["relations"])

    # identified_relation_num += len(result[i]["relations"])

    gt_list = []
    pred_list = []
    for j in gold_result[i]["relations"]:
        pair_dict = {}
        pair_dict["one_event_id"] = j["one_event"]["id"]
        pair_dict["other_event_id"] = j["other_event"]["id"]
        pair_dict["relation_type"] = j["relation_type"]
        gt_list.append(pair_dict)

    # 统计因果关系预测结果
    for k, v in pred_result[i]["causal_relations"].items():
        if v:
            for pair in v:
                temp_pair_dict = {}
                temp_pair_dict["one_event_id"] = pair[0]
                temp_pair_dict["other_event_id"] = pair[1]
                temp_pair_dict["relation_type"] = "时序"
                pred_list.append(temp_pair_dict)

    # 统计时序关系预测结果
    for k, v in pred_result[i]["temporal_relations"].items():
        if v:
            for pair in v:
                temp_pair_dict = {}
                temp_pair_dict["one_event_id"] = pair[0]
                temp_pair_dict["other_event_id"] = pair[1]
                temp_pair_dict["relation_type"] = "时序"
                pred_list.append(temp_pair_dict)

    identified_relation_num += len(pred_list)

    for item in pred_list:
        if item in gt_list:
            TP += 1
            gt_list.remove(item)


P = TP/identified_relation_num
R = TP/annotated_relation_num
F1 = (2*P*R)/(P+R)
print(P, R, F1)
print(identified_relation_num, annotated_relation_num)
print(TP)



