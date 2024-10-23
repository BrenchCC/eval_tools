from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import MATHDataset, MATHEvaluator, math_postprocess_v2_agentic, normalize_final_answer, math_postprocess_v2

math_reader_cfg = dict(input_columns=['problem'], output_column='solution')

math_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=dict(
                role='SYSTEM',
                prompt='''You are a world-class AI system, capable of complex reasoning and reflection. Outlining the initial problem and related factors through the query inside <thinking> tags, 
                engages in a series of reflection steps and analyzing different aspects of the problem inside <reflection> tags. 
                Finally, based on the thinking and reflections, you generate a well-structured output, providing a clear and actionable solution inside <output> tag.'''
            ),
            round=[
                dict(role='HUMAN', prompt='{problem}\nPlease reason step by step, make sure the final answer is placed within the <output> tag and put your final answer within \\boxed{}.'),
            ]
        ),
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer, max_out_len=1024),
)

# postprocess v2
math_eval_cfg = dict(
    evaluator=dict(type=MATHEvaluator, version='v2'), pred_postprocessor=dict(type=math_postprocess_v2),
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
