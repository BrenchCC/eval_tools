from mmengine.config import read_base

with read_base():
    from ..datasets.mmlu.mmlu_gen_4d595a import mmlu_datasets
    from ..datasets.ceval.ceval_gen_5f30c7 import ceval_datasets
    from ..datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    from ..datasets.humaneval.humaneval_gen_8e312c import humaneval_datasets
    from ..datasets.IFEval.IFEval_gen_3321a3 import ifeval_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
