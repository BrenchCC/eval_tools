from mmengine.config import read_base

with read_base():
    from .dataset_collections.xdan_objective import datasets
    from .models.xdan.xdan_models_objective import models
    from .summarizers.chat_OC15_multi_faceted import summarizer
