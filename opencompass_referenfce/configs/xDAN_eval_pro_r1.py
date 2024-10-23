from mmengine.config import read_base

with read_base():
    from .models.xdan.hf_xdan_edge_moe_r1_0815 import models
    # from .models.xdan.xdan_qwen2 import models
    from .dataset_collections.xdan_pro_dataset import datasets
    from .summarizers.chat_OC15_multi_faceted import summarizer
