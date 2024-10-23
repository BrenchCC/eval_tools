from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='hf-xDAN-L1-Edge-MoE-8x1.5b-0814-slim-e1',
        path='/data/vayu/train/models/xDAN-L1-Edge-MoE-8x1.5b-0814-slim-e1',
        max_out_len=1024,
        batch_size=8,
        run_cfg=dict(num_gpus=8),
        stop_words=['<|im_end|>', '<|im_start|>'],
    )
]
