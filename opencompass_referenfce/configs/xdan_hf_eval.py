from mmengine.config import read_base

with read_base():
    from .models.xdan.hf_xdan_qwen2_1_5b import models
    # from .models.qwen.lmdeploy_qwen2_1_5b_instruct.py import models
    #from .dataset_collections.data import datasets
    from .datasets.collections.chat_core import datasets
    from .summarizers.leaderboard import summarizer
