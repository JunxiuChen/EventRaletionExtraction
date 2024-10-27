from zhipuai import ZhipuAI
import json
from utils import *
import time, random

client = ZhipuAI(api_key="dff8037e8a7b540e96c62a80315c5462.spn2ArDpZQmSk5Zl")

def invoke_example(prompt):
    response = client.chat.completions.create(
        model="glm-4-0520",
        messages=prompt,
        top_p=0.7,
        temperature=0.95,
        max_tokens=4096,
    )
    # print(response)
    return response


def main():
    test_data = load_line_data('../data/testa.json')
    save_file = '../output/test_response.json'
    for item in test_data:
        id = item["new-ID"]
        event_type = item["event_type"]
        passage = item["doc"]
        event_list = item["events"]
        prompt_content = f'''你是一个优秀的事件关系抽取模型，现在需要你从给定的一篇文章中找出各个事件之间是否存在因果关系或时序关系，给定文章中包含的事件列表为：{event_list}，给定的文章如下：\"{passage}\"，请你找出所有事件之间的因果关系或时序关系，每个事件对只存在一种关系，无需给出理由，请直接输出答案，格式为“（事件1，事件2，关系）”。'''
        prompt = [{"role": "user", "content": prompt_content}]
        print(prompt)
        # try:
        #     response = invoke_example(prompt)
        #     response_dict = {'new-ID': id, 'output': response.choices[0].message.content}
        #     print(response_dict)
        #     add_response_to_json(save_file, response_dict)
        # except:
        #     response_dict = {'new-ID': id, 'output': "ERROR"}
        #     add_response_to_json(save_file, response_dict)
        break


if __name__ == '__main__':
    main()