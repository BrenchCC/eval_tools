from mmengine.config import read_base

with read_base():
    from .models.qwen.hf_qwen2_1_5b_instruct import models
    from .dataset_collections.xdan_data_1 import datasets
