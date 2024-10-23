from opencompass.models import OpenAI

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

models = [
    dict(
        abbr='Meta-Llama-3.1-70B-Instruct',
        type=OpenAI,
        openai_api_base='http://0.0.0.0:8002/v1/chat/completions', # 服务地址
        path='xDAN-70B-Instruct', # 请求服务时的 model name
        key = 'EMPTY',
        rpm_verbose=True, # 是否打印请求速率
        meta_template=api_meta_template, # 服务请求模板
        query_per_second=32, # 服务请求速率
        max_out_len=1024, # 最大输出长度
        max_seq_len=4096, # 最大输入长度
        temperature=0, # 生成温度
        batch_size=32, # 批处理大小
        retry=100, # 重试次数
        tokenizer_path="../models/Meta-Llama-3.1-70B-Instruct",
    )
]