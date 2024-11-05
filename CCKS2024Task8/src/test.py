# coding=utf-8

# def get_trigger_sent_id(sentences, l, r):
#     num = 0
#     for i, s in enumerate(sentences):
#         if l >= num and l <= num + len(s) and r > num and r <= num + len(s) + 1:
#             # temp_sent_id = i
#             # offset = [l-num, r-num]
#             return [i, [l-num, r-num]]
#             num += len(s)
#         else:
#             num += len(s)
#
#
# a = ['\ufeff2名盗贼踩点尾随官员入室盗窃\n本报讯(记者王鹏昊)男子冯某和赵某，开锁学校毕业后，在昌平某镇政府蹲点跟踪尾随领导，摸清住址后伺机入室盗窃。', '昨天，昌平检察院透露，冯赵二人因涉嫌盗窃已被批捕。', '\n检方指控，男子冯某在唐山一家开锁学校培训期间与同学赵某相识。', '今年五月，来京打工的冯某找到赵某想用二人的开锁技术发财。', '为了不走空，二人将目标锁定为公务员。', '\n按照计划，二人来到昌平某镇政府，在镇政府的公开栏中有多名主要领导的信息及照片，二人用相机拍照记录。', '随后，他们又来到镇政府停车场，发现一辆黑色现代轿车前风挡上，有某小区停车证，他们也用相机拍下车牌和停车证。', '\n当晚，二人便到该小区蹲守。', '几个小时后，他们盯上的轿车驶入小区。', '冯某通过事先拍摄的镇政府工作人员照片，确定为该镇政府一位领导。', '于是，二人尾随这名领导上楼，并记下了该领导家的门牌号。', '一周后，二人又来到该领导家门外，查探其门锁的品牌型号。', '回到暂住地后，二人购买了开锁工具及同领导家一样的门锁试验。', '\n6月初，冯赵二人再次来到该领导家楼下“蹲守”，看到领导及家人离开，按门铃确定没人后，赵某用工具开锁，并负责望风，冯某则进入室内行窃。', '最终，二人盗走近2万现金，及存折、房产证等财物。', '\n6月24日，昌平警方将二人抓获。', '二人称，此前他们还去过延庆县政府踩点，但因该处管理严格，没能进入。']
# l,r = 593,595
# # print(get_trigger_sent_id(a, l, r))
# for i, s in enumerate(a):
#     print(i, s)

# num = 0
# for i,s in enumerate(a):
#     if l>=num and l<=num+len(s) and r>num and r <= num+len(s)+1:
#         print(i)
#         print(l-num, r-num)
#         num += len(s)
#     else:
#         num += len(s)

import re
# text = "﻿2名盗贼踩点尾随官员入室盗窃\n本报讯(记者王鹏昊)男子冯某和赵某，开锁学校毕业后，在昌平某镇政府蹲点跟踪尾随领导，摸清住址后伺机入室盗窃。昨天，昌平检察院透露，冯赵二人因涉嫌盗窃已被批捕。\n检方指控，男子冯某在唐山一家开锁学校培训期间与同学赵某相识。今年五月，来京打工的冯某找到赵某想用二人的开锁技术发财。为了不走空，二人将目标锁定为公务员。\n按照计划，二人来到昌平某镇政府，在镇政府的公开栏中有多名主要领导的信息及照片，二人用相机拍照记录。随后，他们又来到镇政府停车场，发现一辆黑色现代轿车前风挡上，有某小区停车证，他们也用相机拍下车牌和停车证。\n当晚，二人便到该小区蹲守。几个小时后，他们盯上的轿车驶入小区。冯某通过事先拍摄的镇政府工作人员照片，确定为该镇政府一位领导。于是，二人尾随这名领导上楼，并记下了该领导家的门牌号。一周后，二人又来到该领导家门外，查探其门锁的品牌型号。回到暂住地后，二人购买了开锁工具及同领导家一样的门锁试验。\n6月初，冯赵二人再次来到该领导家楼下“蹲守”，看到领导及家人离开，按门铃确定没人后，赵某用工具开锁，并负责望风，冯某则进入室内行窃。最终，二人盗走近2万现金，及存折、房产证等财物。\n6月24日，昌平警方将二人抓获。二人称，此前他们还去过延庆县政府踩点，但因该处管理严格，没能进入。随后，二人来到附近一个卫生服务站，并趁一间办公室无人之机，入室盗走一台笔记本电脑"
# split_sentences = [sent for sent in re.split('(。|！|\!|\.|？|\?)', text) if sent]
# sentences = []
# sent = split_sentences[0]
# for i in range(1, len(split_sentences)):
#     if len(split_sentences[i]) == 1:
#         sent += split_sentences[i]
#         sentences.append(sent)
#         sent = ''
#     else:
#         sent += split_sentences[i]
# sentences.append(sent)
# print(sentences)
import json
def load_line_data(path):
    data = []
    with open(path, 'r', encoding='utf-8') as f:
        line_data = f.readlines()
        for line in line_data:
            dic = json.loads(line)
            data.append(dic)
    return data
event_type_id = load_line_data('../data/maven_format_data/event_type_id.json')
print(event_type_id)
print(type(event_type_id[0]))