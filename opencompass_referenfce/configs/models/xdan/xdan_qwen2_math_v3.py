from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-1.5b-Reasoning-math-v3-0815-e2',
        path='/data/vayu/train/models/xDAN-L1-Edge-1.5b-Reasoning-math-v3-0815-e2',
        max_out_len=2048,
        batch_size=8,
        run_cfg=dict(num_gpus=2),
    )
]
