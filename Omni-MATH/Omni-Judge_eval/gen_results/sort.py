import json
data = []

file_name= 'xDAN-L3-Agentic-Reflection-Math-0919-liger-Instruct-v3-e3'
with open(file_name+'.jsonl', 'r') as f:
    for line in f:
        data.append(json.loads(line))

sorted_data = sorted(data, key=lambda x: x['id'])

for item in sorted_data:
    with open(file_name+'-sorted.jsonl','a') as f:
        json_line = json.dumps(item)
        f.write(json_line + '\n')
