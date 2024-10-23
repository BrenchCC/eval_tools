from mmengine.config import read_base

with read_base():
    from .models.hf_llama.hf_llama3_8b_instruct import models
    from .dataset_collections.xdan_data_1 import datasets
