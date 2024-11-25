import json
import re
import os

def load_data(path):
    '''
    加载数据
    :param path:
    :return:
    '''
    with open(path, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    return data


def load_line_data(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        line_data = f.readlines()
        for line in line_data:
            dic = json.loads(line)
            data.append(dic)
    return data

def save_data_bylines(all_data, save_path):
    print(save_path, "正在写入文件....")
    with open(save_path, 'w', encoding='utf-8') as jf:
        for item in all_data:
            jf.write(json.dumps(item)+'\n')
        print(save_path, "文件写入成功！")

def save_data_indent(all_data, save_path):
    print(save_path, "正在保存文件....")
    with open(save_path, 'w', encoding='utf-8') as jf:
        jf.write(json.dumps(all_data, indent=4, ensure_ascii=False))
        print(save_path, "文件写入成功！")

def add_response_to_json(path, new_data):
    with open(path, 'a', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False)
        f.write('\n')


def get_event_num_dic(path):  # '../data/RAMS/event_num.txt'
    '''
    获得事件类型数量
    :param path:
    :return:
    '''
    train_event_num_dic = {}
    with open(path, encoding='utf-8') as f:
        train_events = f.readlines()[0]
        train_events = eval(train_events)["train"] # 列表

    for i in train_events:
        train_event_num_dic[i[0]] = i[1]
    return train_event_num_dic


def get_event_schema(path):  # '../data/RAMS/labels.json'
    '''
    获得事件模式
    :param path:
    :return:
    '''
    with open(path, encoding='utf-8') as f:
        event_schema = json.loads(f.read())
    return event_schema

def contains_chinese(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]')  # 匹配中文字符的正则表达式
    return bool(pattern.search(text))  # 检测字符串中是否包含中文字符

def find_all_positions(str, char):
    '''
    查找指定字符的所有位置
    :param str:
    :param char:
    :return:
    '''
    positions = []
    index = -1
    while True:
        index = str.find(char, index+1)
        if index==-1:
            break
        positions.append(index)
    return positions


def get_event_type_dict(data):
    event_type_dict = {}
    for item in data:
        event_type = item["evt_triggers"][0][2][0][0]
        if event_type not in event_type_dict.keys():
            event_type_dict[event_type] = 1
        else:
            event_type_dict[event_type] += 1
    # event_type_dict = sorted(event_type_dict.items(), key=lambda x:x[1], reverse=True)
    return event_type_dict


def get_role_type_dict(data):
    role_type_dict = {}
    for item in data:
        gold_evt_links = item["gold_evt_links"]
        for i in gold_evt_links:
            role = i[-1][11:]
            if role not in role_type_dict.keys():
                role_type_dict[role] = 1
            else:
                role_type_dict[role] += 1

    # role_type_dict = sorted(role_type_dict.items(), key=lambda x: x[1], reverse=True)
    return role_type_dict


def get_name(sentences, sidx, eidx):
    pasg = ''
    for sent in sentences:
        pasg = pasg + ' ' + ' '.join(sent)
    pasg = pasg.strip(' ')

    name = pasg.split(' ')[sidx:eidx+1]
    return ' '.join(name)


def get_passage(sentences):
    pasg = ''
    for sent in sentences:
        pasg = pasg + ' ' + ' '.join(sent)
    pasg = pasg.strip(' ')
    return pasg


def get_complete_sample(train_data, event_shcema):
    '''
    从训练集中找出具有完整事件论元角色的样本用作参考示例
    :return: {event_type1:[[passage1, arg_dic1], [], []...], event_type2:[[passage2, arg_dic2], [], []...],...}
    '''
    complete_examples = {}
    uncomplete_examples = {}
    for item in train_data:
        event_type = item["evt_triggers"][0][2][0][0]
        args = item["gold_evt_links"]
        if len(args) == len(event_shcema[event_type]):
            if event_type not in complete_examples.keys():
                complete_examples[event_type] = []
                complete_examples[event_type].append(item)
            else:
                complete_examples[event_type].append(item)
        else:
            if event_type not in uncomplete_examples.keys():
                uncomplete_examples[event_type] = []
                uncomplete_examples[event_type].append(item)
            else:
                uncomplete_examples[event_type].append(item)

    return complete_examples, uncomplete_examples

def which_snt(snt2span, span):  # snt2span:[[s_1, e_1], [s_2, e_2],...]
    for snt in range(len(snt2span)):
        snt_spans = snt2span[snt]
        if span[0] >= snt_spans[0] and span[1] <= snt_spans[1]:
            return snt
    assert False


