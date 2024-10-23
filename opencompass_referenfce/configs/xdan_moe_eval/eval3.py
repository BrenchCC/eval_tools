from mmengine.config import read_base

with read_base():
    from ..models.xdan_moe.model3 import models
    from ..dataset_collections.xdan_data_shot import datasets
    from ..summarizers.chat_OC15_multi_faceted import summarizer
