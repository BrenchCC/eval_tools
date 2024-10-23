from mmengine.config import read_base

with read_base():
    from ..mmlu.mmlu_gen_4d595a import mmlu_datasets
    from ..cmmlu.cmmlu_gen_c13365 import cmmlu_datasets
    from ..ceval.ceval_internal_ppl_1cd8bf import ceval_datasets
    from ..GaokaoBench.GaokaoBench_no_subjective_gen_4c31db import GaokaoBench_datasets
    from ..triviaqa.triviaqa_wiki_1shot_gen_bc5f21 import triviaqa_datasets
    from ..nq.nq_open_1shot_gen_2e45e5 import nq_datasets
    from ..race.race_gen_69ee4f import race_datasets
    from ..winogrande.winogrande_5shot_gen_6447e6 import winogrande_datasets
    from ..hellaswag.hellaswag_10shot_gen_e42710 import hellaswag_datasets
    from ..bbh.bbh_gen_5b92b0 import bbh_datasets
    from ..gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    from ..math.math_evaluatorv2_gen_cecb31 import math_datasets
    from ..TheoremQA.TheoremQA_gen import TheoremQA_datasets
    from ..humaneval.humaneval_gen_8e312c import humaneval_datasets
    from ..mbpp.mbpp_gen_830460 import mbpp_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
