from opencompass.models import HuggingFacewithChatTemplate,HuggingFaceBaseModel

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

models = [
    dict(
        type=HuggingFacewithChatTemplate,
        abbr='xDAN-L1-Edge-4x1.5b-reasoning-pro-0827',
        path='../models/xDAN-L1-Edge-4x1.5b-reasoning-pro-0827',
        meta_template=api_meta_template,
        max_out_len=4096,
        batch_size=10,
        run_cfg=dict(num_gpus=1),
    )
]

