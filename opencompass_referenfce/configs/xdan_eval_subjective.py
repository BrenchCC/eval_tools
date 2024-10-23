from mmengine.config import read_base

with read_base():
    from .dataset_collections.xdan_subjective import datasets
    from .models.xdan.xdan_models_subjective import models,judge_models,eval
    from .summarizers.subjective import summarizer
