from opencompass.models import TurboMindModelwithChatTemplate
from opencompass.models import LmdeployPytorchModel

models = [
    dict(
        type=LmdeployPytorchModel,
        abbr='xDAN-L1-Edge-MoE-4x1.5b-0814',
        path='/data/vayu/train/models/xDAN-L1-Edge-MoE-4x1.5b-0814',
        engine_config=dict(session_len=7168, max_batch_size=16, tp=2),
        gen_config=dict(top_k=1, temperature=1e-6, top_p=0.9, max_new_tokens=1024),
        max_seq_len=7168,
        max_out_len=2048,
        batch_size=8,
        run_cfg=dict(num_gpus=2)
    )
]
