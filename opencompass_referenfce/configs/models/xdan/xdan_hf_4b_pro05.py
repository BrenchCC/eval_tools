from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-4b-pro05',
        path='/data/vayu/train/models/xDAN-L1-Edge-4b-pro-05',
        max_out_len=2048,
        batch_size=8,
        run_cfg=dict(num_gpus=8),
        stop_words=['<|end_of_text|>', '<|eot_id|>'],
    )
]
