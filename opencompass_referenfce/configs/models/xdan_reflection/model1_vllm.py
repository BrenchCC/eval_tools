from opencompass.models import OpenAI,OpenAISDK

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

models = [
    dict(
        abbr='xDAN-L3-Reflection-checkpoint-413',
        type=OpenAI,
        openai_api_base='http://0.0.0.0:8005/v1/chat/completions', # 服务地址
        path='xDAN-L3-Reflection-checkpoint-413', # 请求服务时的 model name
        key = 'EMPTY',
        rpm_verbose=True, # 是否打印请求速率
        meta_template=api_meta_template, # 服务请求模板
        query_per_second=8, # 服务请求速率
        max_out_len=1024, # 最大输出长度
        max_seq_len=4096, # 最大输入长度
        temperature=0.7, # 生成温度
        batch_size=64, # 批处理大小
        retry=1000, # 重试次数
        tokenizer_path="../models/checkpoint-413",
    )
]
