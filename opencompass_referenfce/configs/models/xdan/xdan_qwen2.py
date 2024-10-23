from opencompass.models import HuggingFacewithChatTemplate
from opencompass.models import LmdeployPytorchModel
from opencompass.models import Qwen
from opencompass.models import VLLM,VLLMwithChatTemplate
from opencompass.models import HuggingFaceCausalLM,HuggingFaceBaseModel
models = [
    dict(
        #type = HuggingFaceBaseModel,
        #type=HuggingFacewithChatTemplate,
        # type = HuggingFaceCausalLM,
        type = LmdeployPytorchModel,
        abbr='qwen-2',
        # path='modelspace/xDAN-L1-Edge-8x1.5b-kd-MoE-0813',
        path = 'modelspace/xDAN-L1-Edge-MoE-4x1.5b-0813',
        # path = 'modelspace/xDAN-L1-Edge-1.5b-mag-ultra-0812-e05',
        # max_seq_len=2048,
        max_out_len=1024,
        batch_size=8,
        run_cfg=dict(num_gpus=1),
    )
]
