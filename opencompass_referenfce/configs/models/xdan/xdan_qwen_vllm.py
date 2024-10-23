from opencompass.models import VLLMwithChatTemplate

models = [
    dict(
        type=VLLMwithChatTemplate,
        abbr='xdan_qwen2-8x1_5b-instruct-vllm',
        path='../models/xDAN-L1-Edge-8x1.5b-kd-MoE-0813',
        model_kwargs=dict(tensor_parallel_size=1),
        max_out_len=1024,
        batch_size=32,
        generation_kwargs=dict(temperature=0),
        run_cfg=dict(num_gpus=1),
    )
]
