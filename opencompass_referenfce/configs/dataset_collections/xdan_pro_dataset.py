from mmengine.config import read_base

with read_base():
    from ..datasets.mmlu.mmlu_gen_4d595a import mmlu_datasets
    from ..datasets.mmlu_pro.mmlu_pro_gen_cdbebf import mmlu_pro_datasets
    from ..datasets.ceval.ceval_gen_5f30c7 import ceval_datasets
    from ..datasets.bbh.bbh_gen_2879b0 import bbh_datasets
    from ..datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    from ..datasets.humaneval.humaneval_gen_8e312c import humaneval_datasets
    from ..datasets.math.math_0shot_gen_393424 import math_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
