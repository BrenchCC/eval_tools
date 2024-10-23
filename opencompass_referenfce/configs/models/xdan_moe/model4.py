from opencompass.models import HuggingFacewithChatTemplate
models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-MoE-4x1.5b-r41',
        path='moe_models/xDAN-L1-Edge-MoE-4x1.5b-r41',
        max_out_len=4096,
        batch_size=8,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]
