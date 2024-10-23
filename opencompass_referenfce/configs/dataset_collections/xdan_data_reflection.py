from mmengine.config import read_base

with read_base():
    from ..datasets.gpqa.gpqa_reflection import gpqa_datasets
    from ..datasets.mmlu.mmlu_reflection import mmlu_datasets
    from ..datasets.humaneval.humaneval_reflection import humaneval_datasets
    from ..datasets.math.math_reflection import math_datasets
    from ..datasets.gsm8k.gsm8k_reflection import gsm8k_datasets
    from ..datasets.IFEval.IFEval_reflection import ifeval_datasets


datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
