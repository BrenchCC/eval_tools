from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-1.5b-Reasoning-v2-0813-e2',
        path='/data/vayu/train/models/xDAN-L1-Edge-1.5b-Reasoning-v2-0813-e2',
        max_out_len=2048,
        batch_size=64,
        run_cfg=dict(num_gpus=1),
    )
]
