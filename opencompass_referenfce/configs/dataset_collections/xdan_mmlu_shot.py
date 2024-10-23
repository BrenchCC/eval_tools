from mmengine.config import read_base
with read_base():
    #from ..datasets.mmlu.xdan_mmlu_shot2 import mmlu_datasets
    #from ..datasets.mmlu.xdan_mmlu_shot import mmlu_datasets
    from ..datasets.mmlu.xdan_mmlu_shot3 import mmlu_datasets
datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
