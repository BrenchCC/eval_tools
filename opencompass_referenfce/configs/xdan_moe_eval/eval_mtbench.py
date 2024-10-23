from mmengine.config import read_base

with read_base():
    from ..datasets.subjective.alignbench.alignbench_judgeby_critiquellm import alignbench_datasets
    from ..datasets.subjective.multiround.mtbench_single_judge_diff_temp import mtbench_datasets
    from ..datasets.subjective.arena_hard.arena_hard_compare import arenahard_datasets
from opencompass.models import HuggingFaceCausalLM, HuggingFace, HuggingFaceChatGLM3, OpenAI
from opencompass.partitioners import NaivePartitioner, SizePartitioner
from opencompass.partitioners.sub_naive import SubjectiveNaivePartitioner
from opencompass.partitioners.sub_size import SubjectiveSizePartitioner
from opencompass.partitioners.sub_num_worker import SubjectiveNumWorkerPartitioner
from opencompass.runners import LocalRunner
from opencompass.runners import SlurmSequentialRunner
from opencompass.tasks import OpenICLInferTask
from opencompass.tasks.subjective_eval import SubjectiveEvalTask
from opencompass.summarizers import SubjectiveSummarizer

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

# -------------Inference Stage ----------------------------------------
# For subjective evaluation, we often set do sample for models
models = [
    dict(
        type=OpenAI,
        abbr='xDAN-L1-Edge-4x1.5b-reasoning-pro-0827',
        path='xDAN-L1-Edge-4x1.5b-reasoning-pro-0827',
        openai_api_base='http://0.0.0.0:8080/v1/chat/completions', # 服务地址
        key='EMPTY',
        query_per_second=16,
        rpm_verbose=True,  # 是否打印请求速率
        tokenizer_path='../models/xDAN-L1-Edge-4x1.5b-reasoning-pro-0827',
        meta_template=api_meta_template,
        max_out_len=2048,
        max_seq_len=4096,
        retry=200,
        batch_size=256,
    )
]


datasets = [*alignbench_datasets] # add datasets you want


infer = dict(
    partitioner=dict(type=NaivePartitioner),
    runner=dict(type=LocalRunner, max_num_workers=16, task=dict(type=OpenICLInferTask)),
)
# -------------Evalation Stage ----------------------------------------

## ------------- JudgeLLM Configuration
judge_models = [dict(
    abbr='gpt-4o',
    type=OpenAI,
    openai_api_base='http://35.240.173.116:7220//v1/chat/completions',
    path='gpt-4o',
    key='sk-MlDxlbyaiUbD1mWo43089dAa82204b07AaEf409c6e256f07',  # The key will be obtained from $OPENAI_API_KEY, but you can write down your key here as well
    meta_template=api_meta_template,
    query_per_second=1,
    max_out_len=2048,
    max_seq_len=2048,
    batch_size=8,
    temperature=0,
    retry=100,
)]
'''
judge_models = [dict(
    abbr='Qwen2-7B-Instruct',
    type=OpenAI,
    openai_api_base='http://0.0.0.0:8081/v1/chat/completions',
    path='Qwen2-7B-Instruct',
    key='EMPTY',  # The key will be obtained from $OPENAI_API_KEY, but you can write down your key here as well
    meta_template=api_meta_template,
    query_per_second=16,
    max_out_len=2048,
    rpm_verbose=True,
    max_seq_len=2048,
    batch_size=12,
    retry=200,
    temperature=0,
    tokenizer_path='../models/Qwen2-7B-Instruct'
)]
'''
## ------------- Evaluation Configuration
eval = dict(
    partitioner=dict(type=SubjectiveNaivePartitioner, models=models, judge_models=judge_models,),
    runner=dict(type=LocalRunner, max_num_workers=16, task=dict(type=SubjectiveEvalTask)),
)

summarizer = dict(type=SubjectiveSummarizer, function='subjective')
work_dir = 'mmlu_strengthen/xDAN-L1-Edge-4x1.5b-reasoning-pro-0827-subjective-Q4'
#work_dir = 'moe_eval/Qwen2-1.5B-Instruct'
