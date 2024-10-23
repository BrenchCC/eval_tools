from mmengine.config import read_base

with read_base():
    from ..models.xdan_moe.model7_vllm import models
    from ..dataset_collections.xdan_data_moe import datasets
    from ..summarizers.chat_OC15_multi_faceted import summarizer
