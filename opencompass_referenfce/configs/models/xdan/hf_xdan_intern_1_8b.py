from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-1.8b-reasoning-chat-0814',
        path='/data/vayu/train/models/xDAN_L1_Edge_1_8b_reasoning_chat_0814',
        max_out_len=1024,
        batch_size=16,
        run_cfg=dict(num_gpus=8),
    )
]


#/data/vayu/train/models/xDAN-L1-Edge-1.8b-reasoning-chat-0814
