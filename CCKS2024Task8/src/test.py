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
a = ["柬埔寨茶胶省前省长赖万那涉嫌杀害国会女官员被捕_澎湃国际_澎湃新闻-ThePape。", "\n\n中新网金边4月1日消息，柬埔寨茶胶省前省长赖万那涉嫌杀害国会女官员,1日被捕。", "柬官方向媒体表示，当日赖万那被撤换茶胶省人民党主席一职，并在交接仪式后乘车离开约150米处就被4辆车子拦截。", "车内走出几名警员，当场出示金边初级法院副检察官祥宋签发的拘捕令，随后将赖万那带上警车。", "拘捕令显示，赖万那，45岁，柬内政部官员、茶胶省前任省长，20日前必须接受警察总署刑事警察局审讯。", "3月31日晚，赖万那在其官网发帖，承认与被害国会女官员有“婚外情”，但没有杀害死者。", "他称自己与死者交往一年多后分手，可能导致死者伤心走上“不归路”。", "赖万那在官网强调，自己与哥哥(已被捕的该省副警察长赖纳乐)不是“杀人魔”。", "柬内政部发言人乔速比表示，根据警方调查显示，赖万那是幕后真凶，而死者生前的密友也证实赖万那是背后主谋。", "死者赵素婉尼(女，36岁)，柬国会官员，柬人民党海外青年运动成员，居住柬茶胶省敦胶市。", "今年1月26日，警方在死者住宅卧室发现其上吊自杀。", "乔速比称，该省警方以“自杀”结案，最终被排除自杀对案件侦查，锁定并逮捕包括柬茶胶省副警察长赖纳乐及其他7名涉案警官。", "乔速比表示，3月31日下午，赖纳乐等涉案人已被押往金边初级法院接受审讯。", "（原题为《柬茶胶省前省长涉嫌杀害国会女官员被捕》）"]
l,r = 391,392
# print(get_trigger_sent_id(a, l, r))
# for i, s in enumerate
num = 0
for i,s in enumerate(a):
    if l>=num and l<num+len(s) and r>l and r <= num+len(s):
        print(i)
        print(l-num, r-num)
        num += len(s)
    else:
        num += len(s)

import re
# split_sentences = ["柬埔寨茶胶省前省长赖万那涉嫌杀害国会女官员被捕_澎湃国际_澎湃新闻-ThePape。", "\n\n中新网金边4月1日消息，柬埔寨茶胶省前省长赖万那涉嫌杀害国会女官员,1日被捕。", "柬官方向媒体表示，当日赖万那被撤换茶胶省人民党主席一职，并在交接仪式后乘车离开约150米处就被4辆车子拦截。", "车内走出几名警员，当场出示金边初级法院副检察官祥宋签发的拘捕令，随后将赖万那带上警车。", "拘捕令显示，赖万那，45岁，柬内政部官员、茶胶省前任省长，20日前必须接受警察总署刑事警察局审讯。", "3月31日晚，赖万那在其官网发帖，承认与被害国会女官员有“婚外情”，但没有杀害死者。", "他称自己与死者交往一年多后分手，可能导致死者伤心走上“不归路”。", "赖万那在官网强调，自己与哥哥(已被捕的该省副警察长赖纳乐)不是“杀人魔”。", "柬内政部发言人乔速比表示，根据警方调查显示，赖万那是幕后真凶，而死者生前的密友也证实赖万那是背后主谋。", "死者赵素婉尼(女，36岁)，柬国会官员，柬人民党海外青年运动成员，居住柬茶胶省敦胶市。", "今年1月26日，警方在死者住宅卧室发现其上吊自杀。", "乔速比称，该省警方以“自杀”结案，最终被排除自杀对案件侦查，锁定并逮捕包括柬茶胶省副警察长赖纳乐及其他7名涉案警官。", "乔速比表示，3月31日下午，赖纳乐等涉案人已被押往金边初级法院接受审讯。", "（原题为《柬茶胶省前省长涉嫌杀害国会女官员被捕》）"]
# # split_sentences = [sent for sent in re.split('(。|！|\!|？|\?)', text) if sent]
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




# import json
# def load_line_data(path):
#     data = []
#     with open(path, 'r', encoding='utf-8') as f:
#         line_data = f.readlines()
#         for line in line_data:
#             dic = json.loads(line)
#             data.append(dic)
#     return data
# event_type_id = load_line_data('../data/maven_format_data/event_type_id.json')
# print(event_type_id)
# print(type(event_type_id[0]))