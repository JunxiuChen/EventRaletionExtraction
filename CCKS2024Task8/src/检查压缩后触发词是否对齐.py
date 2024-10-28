from utils import *

# ori_data = load_line_data("../data/train.json")
# compress_data = load_line_data("../output/compress_output/compress_train1.json")

ori_data = load_line_data("../data/testb.json")
compress_data = load_line_data("../output/compress_output/compress_testb1.json")
n = len(ori_data)

correct = 0
for i in range(n):
    ori_events = ori_data[i]["events"]
    gold_triggers = []
    for event in ori_events:
        trigger = event["event-information"]["trigger"][0]["text"]
        gold_triggers.append(trigger)
    # print(gold_triggers)
    output = compress_data[i]["output"]
    # 使用正则表达式匹配 <>
    pattern = r'<(.*?)>'
    # 找到所有匹配的内容
    matches = re.findall(pattern, output)
    # print(matches)

    if gold_triggers == matches:
        correct += 1

print(correct, n-correct)
# train:3204 4796
# testa:404 596
# testb:394 606

