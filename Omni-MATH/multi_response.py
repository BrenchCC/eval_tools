import json
from openai import OpenAI
from tqdm import tqdm  # 引入tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

data = []
# 读取数据
with open('Omni-Math.jsonl', 'r') as f:
    for line in f:
        data.append(json.loads(line))

# client = OpenAI(api_key='sk-MlDxlbyaiUbD1mWo43089dAa82204b07AaEf409c6e256f07', base_url='http://35.240.173.116:7220/v1')
client = OpenAI(api_key='EMPTY', base_url='http://0.0.0.0:8003/v1')
model_name = client.models.list().data[0].id

system_prompt = ("You are an artificial intelligence mathematics expert with complex reasoning and reflection abilities. You are responsible for helping users solve mathematical problems."
                 "Let's think step by step and finally give a final answer that conforms to mathematical specifications.")

def process_problem(i, current_data):
    problem = current_data['problem']
    response = client.chat.completions.create(
        #model='gpt-4o-mini',
        model='xDAN-L3-Agentic',
        messages=[
            {
                'role': 'system',
                'content': system_prompt
            },
            {
                'role': 'user',
                'content': problem
            },
        ],
        temperature=0.9,
    )
    answer = response.choices[0].message.content

    temp_dict = {
        "id": i,
        "domain": current_data['difficulty'],
        "difficulty": current_data['difficulty'],
        "problem": current_data['problem'],
        "answer": current_data['answer'],
        "source": current_data['source'],
        "model_generation": answer
    }
    return temp_dict

# 检查现有文件并获取最大ID
existing_ids = set()
if os.path.exists('Omni-Judge_eval/gen_results/xDAN-L3-Agentic-Reflection-Math-0919-liger-Instruct-v3-e3.jsonl'):
    with open('Omni-Judge_eval/gen_results/xDAN-L3-Agentic-Reflection-Math-0919-liger-Instruct-v3-e3.jsonl', 'r') as f:
        for line in f:
            existing_ids.add(json.loads(line)['id'])

# 从最大ID + 1 开始处理
start_id = max(existing_ids) + 1 if existing_ids else 0

with open('Omni-Judge_eval/gen_results/xDAN-L3-Agentic-Reflection-Math-0919-liger-Instruct-v3-e3.jsonl', 'a') as f:
    with ThreadPoolExecutor(max_workers=32) as executor:  # 创建线程池，限制最大并发数为32
        future_to_data = {executor.submit(process_problem, i, data[i]): i for i in range(start_id, len(data))}
        for future in tqdm(as_completed(future_to_data), total=len(future_to_data), desc="Processing Omni-Math"):
            try:
                result = future.result()
                json_line = json.dumps(result)
                f.write(json_line + '\n')
            except Exception as e:
                print(f"Error processing problem {future_to_data[future]}: {e}")
