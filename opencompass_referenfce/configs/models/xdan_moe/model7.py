from opencompass.models import HuggingFacewithChatTemplate
models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-MoE-4x1.5b-s41-random',
        path='moe_models/xDAN-L1-Edge-MoE-4x1.5b-s41-random',
        max_out_len=2048,
        batch_size=8,
        run_cfg=dict(num_gpus=1),
    )
]
