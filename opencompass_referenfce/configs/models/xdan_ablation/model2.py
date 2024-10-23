from opencompass.models import HuggingFacewithChatTemplate
meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)
models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-1.5b-Reasoning-0825-mmlu-pro-e3',
        path='../models/xDAN-L1-Edge-1.5b-Reasoning-0825-mmlu-pro-e3',
        meta_template=meta_template,
        max_out_len=1024,
        batch_size=8,
        run_cfg=dict(num_gpus=1),
        models_kwargs=dict(attn_implementation="flash_attention_2"),
    )
]
