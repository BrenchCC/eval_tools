from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-1.5b-Reasoning-0825-mmlu-pro-e3',
        path='../models/xDAN-L1-Edge-1.5b-Reasoning-0825-mmlu-pro-e3',
        max_out_len=1024,
        batch_size=16,
        run_cfg=dict(num_gpus=1),
        models_kwargs=dict(attn_implementation="flash_attention_2"),
    )
]
