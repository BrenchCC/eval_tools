from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-3b-rlhf-0804-e2',
        path='modelspace/xDAN-L1-Edge-3b-rlhf-0804-e2',
        max_out_len=1024,
        batch_size=16,
        run_cfg=dict(num_gpus=1),
    )
]
