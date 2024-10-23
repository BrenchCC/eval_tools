from opencompass.models import HuggingFacewithChatTemplate, OpenAI
from opencompass.partitioners.sub_naive import SubjectiveNaivePartitioner
from opencompass.runners import LocalRunner
from opencompass.tasks.subjective_eval import SubjectiveEvalTask

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
api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

models = []

for i,model in enumerate(model_list):
    model_temp = dict(
        type=HuggingFacewithChatTemplate,
        abbr=model,
        path=f'modelspace/{model}',
        batch_size=4,
        generation_kwargs=dict(
            do_sample=True,  # For subjective evaluation, we suggest you do set do_sample when running model inference!
        ),
        meta_template=api_meta_template,
        max_out_len=2048,
        max_seq_len=4096,
        run_cfg=dict(num_gpus=1, num_procs=1),
    )
    models.append(model_temp)

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)


# -------------Evalation Stage ----------------------------------------

## ------------- JudgeLLM Configuration
judge_models = [dict(
    abbr='Qwen2-7B',
    type=HuggingFacewithChatTemplate,
    path='modelspace/Qwen2-7B-Instruct',
    meta_template=api_meta_template,
    max_out_len=2048,
    max_seq_len=2048,
    batch_size=4,
    temperature=0,
    run_cfg=dict(num_gpus=1, num_procs=1),
)]

## ------------- Evaluation Configuration
eval = dict(
    partitioner=dict(type=SubjectiveNaivePartitioner, models=models, judge_models=judge_models,),
    runner=dict(type=LocalRunner, max_num_workers=16, task=dict(type=SubjectiveEvalTask)),
)
