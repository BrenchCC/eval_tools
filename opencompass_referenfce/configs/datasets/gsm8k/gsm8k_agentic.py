from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import GSM8KDataset, gsm8k_postprocess, gsm8k_dataset_postprocess, Gsm8kEvaluator
from opencompass.datasets import MATHEvaluator, math_postprocess_v2_agentic

gsm8k_reader_cfg = dict(input_columns=['question'], output_column='answer')

gsm8k_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=dict(
                role='SYSTEM',
                prompt= '''You are a world-class AI system, capable of complex reasoning and reflection. Outlining the initial problem and related factors through the query inside <thin>
                engages in a series of reflection steps and analyzing different aspects of the problem inside <reflection> tags. 
                Finally, based on the thinking and reflections, you generate a well-structured output, providing a clear and actionable solution inside <output> tag.'''
            ),
            round=[
                dict(
                    role='HUMAN',
                    prompt='''{question}\nPlease reason step by step\n. Put your final answer(a number or a choice) within \\boxed{}.
                    Your response must follow the following format:
                    <thinking>{content}</thinking>
                    <reflection>{content}</reflection>
                    <output> \\boxed{a number or a choice} </output>
                    '''
                ),
            ],
        ),
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer, max_out_len=512),
)

gsm8k_eval_cfg = dict(
    #evaluator=dict(type=MATHEvaluator, version='v2'),
    #pred_postprocessor=dict(type=math_postprocess_v2_agentic),
    evaluator=dict(type=Gsm8kEvaluator),
    pred_postprocessor=dict(type=gsm8k_postprocess),
    dataset_postprocessor=dict(type=gsm8k_dataset_postprocess),
)

gsm8k_datasets = [
    dict(
        abbr='gsm8k',
        type=GSM8KDataset,
        path='opencompass/gsm8k',
        reader_cfg=gsm8k_reader_cfg,
        infer_cfg=gsm8k_infer_cfg,
        eval_cfg=gsm8k_eval_cfg,
    )
]
