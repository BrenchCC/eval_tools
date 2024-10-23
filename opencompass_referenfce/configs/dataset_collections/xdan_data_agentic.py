from mmengine.config import read_base

with read_base():
    #from ..datasets.humaneval.humaneval_agentic import humaneval_datasets
    from ..datasets.gsm8k.gsm8k_agentic import gsm8k_datasets
    #from ..datasets.math.math_agentic import math_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
