from opencompass.models import HuggingFacewithChatTemplate
models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-MoE-4x1.5b-Slim-DPO-0818',
        path='moe_models/xDAN-L1-Edge-MoE-4x1.5b-Slim-DPO-0818',
        max_out_len=2048,
        batch_size=8,
        run_cfg=dict(num_gpus=1),
    )
]
