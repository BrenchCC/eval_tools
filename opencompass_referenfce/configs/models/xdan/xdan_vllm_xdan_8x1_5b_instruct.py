from opencompass.models import VLLMwithChatTemplate

models = [
    dict(
        type=VLLMwithChatTemplate,
        abbr='xdan_qwen2-8x1_5b-instruct-vllm',
        path='/data/vayu/train/opencompass/models/xDAN-L1-8x1.5b-Finetune-0724-sft-v2-e3',
        model_kwargs=dict(tensor_parallel_size=1),
        max_out_len=1024,
        batch_size=32,
        generation_kwargs=dict(temperature=0),
        run_cfg=dict(num_gpus=1),
    )
]
