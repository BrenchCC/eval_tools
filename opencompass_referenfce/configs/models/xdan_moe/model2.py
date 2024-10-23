from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-4b-Recover-SFT-0817-slim-e03',
        path='../models/xDAN-L1-Edge-4b-Recover-SFT-0817-slim-e03',
        max_out_len=4096,
        batch_size=8,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
]

