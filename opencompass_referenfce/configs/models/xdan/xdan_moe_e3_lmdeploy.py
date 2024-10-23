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
        abbr='xDAN-L1-Edge-MoE-8x1.5b-0814-slim-e3',
        type=OpenAI,
        openai_api_base='http://0.0.0.0:8003/v1', # 服务地址
        path='xDAN-L1-Edge-MoE-8x1.5b-0814-slim-e3', # 请求服务时的 model name
        rpm_verbose=True, # 是否打印请求速率
        key= 'EMPTY',
        meta_template=api_meta_template, # 服务请求模板
        query_per_second=1, # 服务请求速率
        max_out_len=2048, # 最大输出长度
        max_seq_len=8192, # 最大输入长度
        temperature=0, # 生成温度
        batch_size=8, # 批处理大小
        retry=1000, # 重试次数
        tokenizer_path = '/data/vayu/train/models/xDAN-L1-Edge-MoE-8x1.5b-0814-slim-e3',
    )
]
