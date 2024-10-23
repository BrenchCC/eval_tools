from mmengine.config import read_base

with read_base():
    from ..models.xdan_moe.model4_vllm import models
    #from ..datasets.gsm8k.xdan_gsm8k_8shot import gsm8k_datasets as datasets
    #from ..datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets as datasets
    from ..dataset_collections.xdan_data_shot import datasets
    from ..summarizers.chat_OC15_multi_faceted import summarizer
