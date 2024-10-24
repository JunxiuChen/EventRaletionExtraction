from src.utils import *
import re

data = load_line_data('test_response.json')
save_file = 'result.txt'


def get_event_rel_pair(text):
    text = text.replace('(', '（')
    text = text.replace(')', '）')
    text = text.replace(', ', '，')
    p = re.compile(r'[（](.*?)[）]', re.S)
    rel_list = re.findall(p, text)  # 匹配
    rel_list = list(set(rel_list))  # 去重

    relations = []
    for pair in rel_list:
        temp_dic = {}
        pair = pair.split('，')
        if len(pair) != 3:
            continue
        temp_dic["one_event_id"] = pair[0]
        temp_dic["other_event_id"] = pair[1]
        if '时序' in pair[2]:
            temp_dic["relation_type"] = '时序'
        elif '因果' in pair[2]:
            temp_dic["relation_type"] = '因果'
        relations.append(temp_dic)
    return relations


for line in data:
    result = {}
    if line["output"] == "ERROR":
        result["relations"] = []
        add_response_to_json(save_file, result)
        continue
    else:
        result["relations"] = get_event_rel_pair(line["output"])
        add_response_to_json(save_file, result)



