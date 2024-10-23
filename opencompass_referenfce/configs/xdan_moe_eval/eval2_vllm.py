from mmengine.config import read_base

with read_base():
    from ..models.xdan_moe.model2_vllm import models
    #from ..dataset_collections.xdan_data_moe import datasets
    from ..dataset_collections.xdan_data_shot import datasets
    #from ..dataset_collections.xdan_mmlu_shot import datasets
    #from ..datasets.gsm8k.xdan_gsm8k_8shot import gsm8k_datasets as datasets
    from ..summarizers.chat_OC15_multi_faceted import summarizer

