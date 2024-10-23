from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-MoE-8x1.5b-0814-slim-e3-qwen2',
        path='/data/vayu/train/models/xDAN-L1-Edge-MoE-8x1.5b-0814-slim-e3',
        max_out_len=1024,
        batch_size=16,
        run_cfg=dict(num_gpus=8),
    )
]
