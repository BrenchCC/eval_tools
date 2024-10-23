from opencompass.models import HuggingFacewithChatTemplate

model_list = [
    "xDAN-L1-Edge-1.5b-reasoning-e2",
    "xDAN-L1-Edge-1.5b-mag-ultra-0812-e05",
    "xDAN-L1-Edge-4b-instruct-kd-0810",
    "xDAN-L1-Edge-3b-rlhf-0804-e1",
    "xDAN-L1-Edge-3b-rlhf-0804-e2",
    "xDAN-L1-Edge-3b-e2-kd-0803",
    "xDAN-L1-Edge-3b-Instruct-0803-e2",
    "xDAN-L1-Qwen2-Edge-7b-kd",
    "xDAN-L1-Edge-1_8b-instruct-kd-v2-0812",
    "xDAN-L1-Edge-1.5b-Reasoning-v2-0813-e2",
    "xDAN-L1-Edge-MoE-4x1.5b-0813",
    "xDAN-L1-Edge-8x1.5b-kd-MoE-0813",
    ]

models = []

for i,model in enumerate(model_list):
    model_temp = dict(
        type=HuggingFacewithChatTemplate,
        abbr=model,
        path=f'modelspace/{model}',
        max_out_len=1024,
        batch_size=16,
        run_cfg=dict(num_gpus=8,num_proc=8),
    )
    models.append(model_temp)


