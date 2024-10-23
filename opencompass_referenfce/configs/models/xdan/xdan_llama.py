from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='llama-3-3b',
        # path='modelspace/xDAN-L1-Edge-4b-instruct-kd-0810',
        # path = 'modelspace/xDAN-L1-Edge-3b-e2-kd-0803'
        # path = 'modelspace/xDAN-L1-Edge-3b-Instruct-0803-e2'
        path = 'modelspace/xDAN-L1-Edge-3b-rlhf-0804-e1',
        #path = 'modelspace/xDAN-L1-Edge-3b-rlhf-0804-e2',
        max_out_len=1024,
        batch_size=16,
        run_cfg=dict(num_gpus=1),
        stop_words=['<|end_of_text|>', '<|eot_id|>'],
    )
]
