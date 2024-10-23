from mmengine.config import read_base

with read_base():
    from ..datasets.humaneval.humaneval_agentic_sample import humaneval_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
