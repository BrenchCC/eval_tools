from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='hf-xdan-qwen2-1.5b-math',
        path='/data/vayu/train/models/xDAN-L1-Edge-1.5b-Reasoning-math-v3-0815-e2',
        max_out_len=1024,
        batch_size=8,
        run_cfg=dict(num_gpus=8),
        stop_words=['<|im_end|>', '<|im_start|>'],
    )
]
