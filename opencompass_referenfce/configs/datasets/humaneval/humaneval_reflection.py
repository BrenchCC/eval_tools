# THIS SHALL ALSO BE DEPRECATED
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer,SCInferencer
from opencompass.datasets import HumanevalDataset, HumanEvalEvaluator, humaneval_postprocess_v2
generation_kwargs = dict(do_sample=True, temperature=0.7, top_p=0.95)
humaneval_reader_cfg = dict(
    input_columns=['prompt'], output_column='task_id', train_split='test')

# TODO: allow empty output-column
humaneval_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=dict(
                role='SYSTEM',
                prompt='You are a world-class AI system, capable of complex reasoning and reflection. Reason through the query inside <thinking> tags, and then provide your final response inside <output> tags. If you detect that you made a mistake in your reasoning at any point, correct yourself inside <reflection> tags.'
            ),
            round=[
            dict(
                role='HUMAN',
                prompt='You are an intelligent programming assistant to produce Python algorithmic solutions.\nCan you complete the following Python function and do not use <python_tag>?Make sure to put the code in the format like ```python\n your code \n```. \n```python\n{prompt}\n```'),
        ])),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=SCInferencer, max_out_len=1024,generation_kwargs=generation_kwargs,infer_type='sc',sc_size=1))

humaneval_eval_cfg = dict(
    evaluator=dict(type=HumanEvalEvaluator),
    pred_role='BOT',
    k=[1, 10, 100],  # the parameter only for humaneval
    pred_postprocessor=dict(type=humaneval_postprocess_v2),sc_size=1
)

humaneval_datasets = [
    dict(
        abbr='openai_humaneval',
        type=HumanevalDataset,
        path='opencompass/humaneval',
        reader_cfg=humaneval_reader_cfg,
        infer_cfg=humaneval_infer_cfg,
        eval_cfg=humaneval_eval_cfg)
]
