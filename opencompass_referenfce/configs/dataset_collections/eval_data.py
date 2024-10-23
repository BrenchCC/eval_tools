from mmengine.config import read_base

with read_base():
    from ..datasets.mmlu.mmlu_gen_4d595a import mmlu_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
