from utils import *
from copy import deepcopy
import random
data = load_line_data('train.jsonl')
ori_data = deepcopy(data)

for line in data:
    tokens = line["tokens"]
    sentences = line["sentences"]
    events = line["events"]
    timex = line["TIMEX"]
    events_dict = {}
    timex_dict = {}
    for event in events:
        event_id = event["id"]
        events_dict[event_id] = event
    for time in timex:
        event_id = time["id"]
        timex_dict[event_id] = time

    # 屏蔽方法：只屏蔽文本，不屏蔽标签
    masked_events = []
    mask_id = 0
    for k,v in line["temporal_relations"].items():
        for pair in v:
            if pair[0] in masked_events or pair[1] in masked_events:
                continue
            else:
                rand_id = random.randint(0,1)
                mask_event_id = pair[rand_id]
                masked_events.append(mask_event_id)
                if mask_event_id.startswith("EVENT"):
                    sent_id = events_dict[mask_event_id]["mention"][0]["sent_id"]
                    offset = events_dict[mask_event_id]["mention"][0]["offset"]
                    mask_flag = "[MASK_" + str(mask_id) + "]"
                    for i in range(offset[0],offset[1]):
                        tokens[sent_id][i] = mask_flag
                else:
                    sent_id = timex_dict[mask_event_id]["sent_id"]
                    offset = timex_dict[mask_event_id]["offset"]
                    mask_flag = "[MASK_" + str(mask_id) + "]"
                    for i in range(offset[0],offset[1]):
                        tokens[sent_id][i] = mask_flag
                mask_id += 1
    line["tokens"] = tokens

# print(data[0])
# print(ori_data[0])
all_data = ori_data + data
save_data_bylines(all_data, 'train_mask_text_only.jsonl')







