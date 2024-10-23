from opencompass.openicl import SCInferencer
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import HumanevalDataset, HumanEvalEvaluator, humaneval_postprocess_v2

humaneval_reader_cfg = dict(input_columns=['prompt'], output_column='task_id', train_split='test')
generation_kwargs = dict(do_sample=True, temperature=1.0, top_p=0.95)
HUMANEVAL_TEMPLATE = dict(
    round=[
        dict(role='HUMAN', prompt='''Let's think step by step.\nComplete the following python code:\n{prompt}'''),
    ]
)

humaneval_infer_cfg = dict(
    prompt_template=dict(type=PromptTemplate, template=HUMANEVAL_TEMPLATE),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=SCInferencer, max_out_len=2048, generation_kwargs = generation_kwargs, infer_type='sc', sc_size = 8),
)

humaneval_eval_cfg = dict(
    evaluator=dict(type=HumanEvalEvaluator),
    k=[1, 10, 100],
    pred_postprocessor=dict(type=humaneval_postprocess_v2),
    sc_size=8,
)

humaneval_datasets = [
    dict(
        abbr='openai_humaneval',
        type=HumanevalDataset,
        path='opencompass/humaneval',
        reader_cfg=humaneval_reader_cfg,
        infer_cfg=humaneval_infer_cfg,
        eval_cfg=humaneval_eval_cfg,
    )
]
