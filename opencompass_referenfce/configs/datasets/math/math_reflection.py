from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer,SCInferencer
from opencompass.datasets import MATHDataset, MATHEvaluator, math_postprocess_v2, normalize_final_answer

math_reader_cfg = dict(input_columns=['problem'], output_column='solution')
generation_kwargs = dict(do_sample=True, temperature=0.7, top_p=0.95)
math_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=dict(
                role='SYSTEM',
                prompt='You are a world-class AI system, capable of complex reasoning and reflection. Reason through the query inside <thinking> tags, and then provide your final response inside <output> tags. If you detect that you made a mistake in your reasoning at any point, correct yourself inside <reflection> tags.'
            ),
            round=[
                dict(role='HUMAN', prompt='{problem}\nPlease reason step by step, and put your final answer within \\boxed{}.If you use code to solve problem, you must execute your code to get an answer for responding and put your final answer within \\boxed{}.'),
            ]
        ),
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=SCInferencer, max_out_len=4096,generation_kwargs=generation_kwargs,infer_type='sc',sc_size=1),
)

# postprocess v2
math_eval_cfg = dict(
    evaluator=dict(type=MATHEvaluator, version='v2'), pred_postprocessor=dict(type=math_postprocess_v2),sc_size=1
)

math_datasets = [
    dict(
        type=MATHDataset,
        abbr='math',
        path='opencompass/math',
        reader_cfg=math_reader_cfg,
        infer_cfg=math_infer_cfg,
        eval_cfg=math_eval_cfg,
    )
]
