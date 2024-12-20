import json
import re
import os


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
            jf.write(json.dumps(item, ensure_ascii=False)+'\n')
        print(save_path, "文件写入成功！")


def add_response_to_json(path, new_data):
    with open(path, 'a', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False)


def get_trigger_sent_id(sentences, l, r):
    num = 0
    for i, s in enumerate(sentences):
        if l>=num and l<num+len(s) and r>l and r <= num+len(s):
            # temp_sent_id = i
            # offset = [l-num, r-num]
            return [i, [l-num, r-num]]
            num += len(s)
        else:
            num += len(s)

# event_type_id = {}
event_type_id = load_line_data('maven_format_data/event_type_id_add_testa_add_testb.json')[0]
id_count = max(event_type_id.values())+1

<<<<<<< HEAD
# ori_train_data = load_line_data("testb.json")
ori_train_data = load_line_data("补全测试集GT/有GT的测试数据/testb_with_gt.json")
=======
# ori_train_data = load_line_data("train.json")
ori_train_data = load_line_data("补全测试集GT/有GT的测试数据/testa_with_gt.json")
>>>>>>> 6dd3055c8a87563ede8995245381515ba341eacd
all_data = []
for line in ori_train_data:
    text = line["doc"]
    events_list = line["events"]

    split_sentences = [sent for sent in re.split('(。|！|\!|？|\?)', text) if sent]
    sentences = []
    sent = split_sentences[0]
    for i in range(1, len(split_sentences)):
        if len(split_sentences[i]) == 1:
            sent += split_sentences[i]
            sentences.append(sent)
            sent = ''
        else:
            sent += split_sentences[i]
    if sent:
        sentences.append(sent)
    tokens = [list(sentence) for sentence in sentences]
    title = sentences[0]

    events = []
    test_event_mentions = []
    for event in events_list:
        event_dic = {}
        test_event_dic = {}
        event_dic["id"] = event["id"]
        test_event_dic["id"] = event["id"]
        event_type = event["event-information"]["event_type"]
        event_dic["type"] = event_type
        test_event_dic["type"] = event_type
        if event_type not in event_type_id.keys():
            event_type_id[event_type] = id_count
            event_dic["type_id"] = id_count
            test_event_dic["type_id"] = id_count
            # id_count += 1
        else:
            event_dic["type_id"] = event_type_id[event_type]
            test_event_dic["type_id"] = event_type_id[event_type]
        trigger = event["event-information"]["trigger"][0]["text"]

        mention = []
        mention_dic = {}
        mention_dic["id"] = event["id"]
        mention_dic["trigger_word"] = trigger
        test_event_dic["trigger_word"] = trigger
        sent_id_and_offset = get_trigger_sent_id(sentences, event["event-information"]["trigger"][0]["start"], event["event-information"]["trigger"][0]["end"])
        try:
            mention_dic["sent_id"] = sent_id_and_offset[0]
            mention_dic["offset"] = sent_id_and_offset[1]
            test_event_dic["sent_id"] = sent_id_and_offset[0]
            test_event_dic["offset"] = sent_id_and_offset[1]
        except:
            print(sent_id_and_offset)

        mention.append(mention_dic)
        event_dic["mention"] = mention
        events.append(event_dic)
        test_event_mentions.append(test_event_dic)


    # start:处理测试数据时请解除下面代码注释
    line_dic = {}
    line_dic["id"] = line["new-ID"]
    line_dic["title"] = title
    line_dic["tokens"] = tokens
    line_dic["sentences"] = sentences
    line_dic["event_mentions"] = test_event_mentions
    line_dic["TIMEX"] = []
    # end

    # start: 处理训练数据时请解除下面一段代码注释
    # line_dic["id"] = line["new-ID"]
    # line_dic["title"] = title
    # line_dic["tokens"] = tokens
    # line_dic["sentences"] = sentences
    # line_dic["events"] = events
    # line_dic["TIMEX"] = []
    # line_dic["temporal_relations"] = {"时序": []}
    # line_dic["causal_relations"] = {"因果": []}
    #
    # for relation_pair in line["relations"]:
    #     one_event_id = relation_pair["one_event_id"]
    #     other_event_id = relation_pair["other_event_id"]
    #     relation = relation_pair["relation_type"]
    #     if relation == "时序":
    #         line_dic["temporal_relations"]["时序"].append([one_event_id, other_event_id])
    #     elif relation == "因果":
    #         line_dic["causal_relations"]["因果"].append([one_event_id, other_event_id])
    # end

<<<<<<< HEAD
    # start:将带有GT的testa.json作为验证集处理，解除以下代码注释（处理验证数据）
    # line_dic["id"] = line["new-ID"]
    # line_dic["title"] = title
    # line_dic["tokens"] = tokens
    # line_dic["sentences"] = sentences
    # line_dic["events"] = events
    # line_dic["TIMEX"] = []
    #
    # line_dic["temporal_relations"] = {"时序": []}
    # line_dic["causal_relations"] = {"因果": []}
    #
    # for relation_pair in line["relations"]:
    #     one_event_id = relation_pair["one_event"]["id"]
    #     other_event_id = relation_pair["other_event"]["id"]
    #     relation = relation_pair["relation_type"]
    #     if relation == "时序":
    #         line_dic["temporal_relations"]["时序"].append([one_event_id, other_event_id])
    #     elif relation == "因果":
    #         line_dic["causal_relations"]["因果"].append([one_event_id, other_event_id])
=======
    # start:将带有GT的testa.json作为验证集处理，解除以下代码注释
    line_dic["temporal_relations"] = {"时序": []}
    line_dic["causal_relations"] = {"因果": []}

    for relation_pair in line["relations"]:
        one_event_id = relation_pair["one_event"]["id"]
        other_event_id = relation_pair["other_event"]["id"]
        relation = relation_pair["relation_type"]
        if relation == "时序":
            line_dic["temporal_relations"]["时序"].append([one_event_id, other_event_id])
        elif relation == "因果":
            line_dic["causal_relations"]["因果"].append([one_event_id, other_event_id])
>>>>>>> 6dd3055c8a87563ede8995245381515ba341eacd
    # end

    all_data.append(line_dic)

# add_response_to_json('maven_format_data/event_type_id_add_testa_add_testb.json', event_type_id)
<<<<<<< HEAD
# save_data_bylines(all_data, 'maven_format_data/valid.jsonl')  # 将testa作为验证集
=======
save_data_bylines(all_data, 'maven_format_data/valid.jsonl')  # 将testa作为验证集

# save_data_bylines(all_data, 'maven_format_data/train.jsonl')
>>>>>>> 6dd3055c8a87563ede8995245381515ba341eacd

# save_data_bylines(all_data, 'maven_format_data/train.jsonl')
save_data_bylines(all_data, 'maven_format_data/test.jsonl')