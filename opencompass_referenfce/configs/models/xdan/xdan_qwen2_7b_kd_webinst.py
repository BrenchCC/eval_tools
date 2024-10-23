from opencompass.models import HuggingFacewithChatTemplate

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xdan_qwen2_7b_kd_webinst-0808',
        path='/data/vayu/train/models/xDAN-L1-Qwen2-Edge-7b-kd-webinst-0808',
        max_out_len=2048,
        batch_size=8,
        run_cfg=dict(num_gpus=4),
    )
]
