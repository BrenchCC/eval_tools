from mmengine.config import read_base

with read_base():
    #from ..datasets.mmlu.mmlu_zero_shot import mmlu_datasets
    #from ..datasets.humaneval.humaneval_zero_shot import humaneval_datasets
    #from ..datasets.humaneval.humaneval_agentic import humaneval_datasets
    #from ..datasets.humaneval.humaneval_gen_8e312c import humaneval_datasets
    from ..datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    #from ..datasets.gsm8k.xdan_gsm8k_8shot import gsm8k_datasets
    #from ..datasets.mmlu_pro.mmlu_pro_0shot_cot_gen_08c1de import mmlu_pro_datasets
    #from ..datasets.mmlu.mmlu_gen_4d595a import mmlu_datasets
    #from ..datasets.math.math_0shot_gen_393424 import math_datasets
    #from ..datasets.ceval.ceval_gen_5f30c7 import ceval_datasets
    #from ..datasets.gpqa.gpqa_openai_simple_evals_gen_5aeece import gpqa_datasets
    #from ..datasets.IFEval.IFEval_gen_3321a3 import ifeval_datasets
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
