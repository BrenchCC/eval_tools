from mmengine.config import read_base

with read_base():
    from ..models.xdan_ablation.model2 import models
    from ..datasets.mmlu.xdan_mmlu_shot1 import mmlu_datasets as datasets
    #from ..datasets.mmlu.mmlu_openai_simple_evals_gen_b618ea import mmlu_datasets as datasets
    #from ..datasets.mmlu.mmlu_gen_4d595a import mmlu_datasets as datasets
    from ..summarizers.chat_OC15_multi_faceted import summarizer
