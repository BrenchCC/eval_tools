from mmengine.config import read_base

with read_base():
    from ..models.xdan_moe.model1_vllm import models
    from ..dataset_collections.xdan_data_sc import datasets
    from ..summarizers.chat_OC15_multi_faceted import summarizer
    #from ..summarizers.mmlu_pro import summarizer
