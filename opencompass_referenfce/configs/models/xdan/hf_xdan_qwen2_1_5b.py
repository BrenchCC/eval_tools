from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xdan-qwen2-1.5b-instruct-hf',
        path='/data/vayu/train/models/xDAN-L1-Edge-1.5b-reasoning-e2',
        max_out_len=2048,
        batch_size=16,
        run_cfg=dict(num_gpus=4),
    )
]
