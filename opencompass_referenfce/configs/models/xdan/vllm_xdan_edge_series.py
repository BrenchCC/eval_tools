from opencompass.models import VLLM

settings = [
    ('xDAN-L1-Edge-1.5b-reasoning-e2-vllm', '/data/vayu/train/models/xDAN-L1-Edge-1.5b-reasoning-e2', 1),
    ('xDAN-L1-Edge-4b-instruct-kd-0810-vllm', '/data/vayu/train/models/xDAN-L1-Edge-4b-instruct-kd-0810', 1)
        ]

models = []
for abbr, path, num_gpus in settings:
    models.append(
        dict(
            type=VLLM,
            abbr=abbr,
            path=path,
            model_kwargs=dict(tensor_parallel_size=num_gpus),
            max_out_len=4096,
            max_seq_len=16384,
            batch_size=8,
            generation_kwargs=dict(temperature=0),
            run_cfg=dict(num_gpus=num_gpus, num_procs=2),
        )
    )
