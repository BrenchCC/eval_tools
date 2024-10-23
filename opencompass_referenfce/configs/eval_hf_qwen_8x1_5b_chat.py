from mmengine.config import read_base

with read_base():
    from .models.qwen.xdan_hf_xdan_8x1_5b_instruct import models
    from .datasets.collections.leaderboard.qwen_chat import datasets
    from .summarizers.leaderboard import summarizer
