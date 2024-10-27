from utils import *
from zhipuai import ZhipuAI
from tqdm import tqdm
client = ZhipuAI(api_key="dff8037e8a7b540e96c62a80315c5462.spn2ArDpZQmSk5Zl")

def invoke_example(prompt):
    response = client.chat.completions.create(
        model="glm-4-0520",
        messages=prompt,
        top_p=0.7,
        temperature=0.95,
    )
    # print(response)
    return response

# data_path = "../data/train.json"
# save_file = "../output/compress_output/compress_1.json"
data_path = "../data/testa.json"
save_file = "../output/compress_output/compress_testa1.json"
data = load_line_data(data_path)

with tqdm(total=len(data)) as p:
    p.set_description("Processing:")
    for i in range(len(data)):
        line = data[i]
        id = line["new-ID"]
        # prompt_content = f"""下面是一条事件关系抽取任务的数据，我需要你帮我压缩关键的事件信息，请返回压缩后的文本，无需多余解释，你必须严格遵守以下要求：（1）压缩后的文本中应该包含原始事件对应的触发词，请使用’<\t>‘在触发词前后进行标记，只能标记给定文本中的触发词，不能多标错标；（2）压缩后的事件必须在逻辑、数量和内容上与原始事件对齐；（3）请保留有利于模型进行事件关系推理的内容，如表示时间、因果关系的词。以下是需要压缩的数据：{line}"""
        prompt_content = f"""给定一条事件关系抽取任务的数据，数据包含文本ID(new-ID)，事件描述的文本(doc)，以及文本中的所有事件(events)，每个事件包含事件id，事件信息包含触发词(trigger)和事件类型(event_type)。
你的任务是对事件描述的文本(doc)进行压缩，要求保留所有事件的关键信息和触发词，并使用<\t>在触发词前后进行标记，请输出压缩后的文本，无需多余解释，你必须严格遵守以下要求：（1）压缩后的文本中应该包含原始事件对应的触发词，不得随意更改事件类型和触发词；（2）压缩后的事件必须在逻辑、数量和内容上与原始事件对齐；（3）请保留有利于模型进行事件关系推理的内容，如表示时间、因果关系的词。
以下是需要压缩的数据：{line}"""
        prompt = [{"role": "system", "content": "你是一个优秀的文本压缩和摘要工具，你能够精准理解用户需求，并给出合理的答案。"},
                  {"role": "user", "content": prompt_content}]
        try:
            response = invoke_example(prompt)
            response_dict = {'new-ID': id, 'output': response.choices[0].message.content}
            print(response_dict)
            add_response_to_json(save_file, response_dict)
        except:
            response_dict = {'new-ID': id, 'output': "ERROR"}
            add_response_to_json(save_file, response_dict)
        p.update(1)










