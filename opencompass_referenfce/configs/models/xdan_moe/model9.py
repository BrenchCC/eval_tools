from opencompass.models import HuggingFacewithChatTemplate
models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-MoE-8x1.5b-0814',
        path='moe_models/xDAN-L1-Edge-MoE-8x1.5b-0814',
        max_out_len=2048,
        batch_size=4,
        run_cfg=dict(num_gpus=1),
    )
]
