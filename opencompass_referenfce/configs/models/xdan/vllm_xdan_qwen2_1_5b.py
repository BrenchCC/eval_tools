from opencompass.models import VLLM

models = [
    dict(
        type=VLLM,
        abbr='xdan-qwen2-1.5b-vllm',
        path='/data/vayu/train/models/xDAN-L1-Edge-1.5b-reasoning-e2',
        model_kwargs=dict(tensor_parallel_size=4),
        max_out_len=1024,
        max_seq_len=8192,
        batch_size=16,
        generation_kwargs=dict(temperature=0),
        run_cfg=dict(num_gpus=4),
    )
]
