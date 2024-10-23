from mmengine.config import read_base

with read_base():
    from .models.xdan.xdan_qwen2_7b_kd_webinst import models
    # from .models.xdan.xdan_qwen2 import models
    from .dataset_collections.xdan_pro_dataset import datasets
    from .summarizers.chat_OC15_multi_faceted import summarizer
