from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-MoE-4x1.5b-0813',
        # path='modelspace/xDAN-L1-Edge-8x1.5b-kd-MoE-0813',
        path = 'modelspace/xDAN-L1-Edge-MoE-4x1.5b-0813',
        # path = 'modelspace/xDAN-L1-Edge-1.5b-mag-ultra-0812-e05',
        # path = 'modelspace/xDAN-L1-Qwen2-Edge-7b-kd',
        max_out_len=1024,
        batch_size=8,
        run_cfg=dict(num_gpus=1),
    )
]
