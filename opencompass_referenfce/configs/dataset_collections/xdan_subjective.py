from mmengine.config import read_base

with read_base():
    from ..datasets.subjective.multiround.mtbench_single_judge_diff_temp import mtbench_datasets
    from ..datasets.subjective.alignbench.alignbench_judgeby_critiquellm import alignbench_datasets

datasets = [*alignbench_datasets, *mtbench_datasets]


