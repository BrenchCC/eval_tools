from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xdan_qwen2-8x1_5b-instruct-hf',
        path='data/vayu/train/opencompass/models/xDAN-L1-8x1.5b-Finetune-0724-sft-v2-e3',
        max_out_len=1024,
        batch_size=16,
        run_cfg=dict(num_gpus=4),
    )
]
