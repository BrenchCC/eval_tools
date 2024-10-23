from opencompass.models import OpenAI

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

models = [
    dict(
        abbr='xDAN-L1-Edge-1.5b-reasoning-e2-API',
        type=OpenAI,
        openai_api_base='http://0.0.0.0:8002/v1',  # Service address
        path='xDAN-L1-Edge-1.5b-reasoning-e2',  # Model name for service request
        rpm_verbose=True,  # Whether to print request rate
        meta_template=api_meta_template,  # Service request template
        query_per_second=1,  # Service request rate
        max_out_len=4096,  # Maximum output length
        max_seq_len=16384,  # Maximum input length
        temperature=0.01,  # Generation temperature
        batch_size=8,  # Batch size
        retry=3,  # Number of retries
    )
]
