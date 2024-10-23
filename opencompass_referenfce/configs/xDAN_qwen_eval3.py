from mmengine.config import read_base

with read_base():
    from .models.xdan.xdan_1 import models
    # from .models.xdan.xdan_qwen2 import models
    from .dataset_collections.xdan_data_1 import datasets
    from .summarizers.chat_OC15_multi_faceted import summarizer
