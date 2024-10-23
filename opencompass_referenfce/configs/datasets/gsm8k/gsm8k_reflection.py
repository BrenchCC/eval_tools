from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer,SCInferencer
from opencompass.datasets import GSM8KDataset, gsm8k_postprocess, gsm8k_dataset_postprocess, Gsm8kEvaluator,MATHEvaluator, math_postprocess_v2

generation_kwargs = dict(do_sample=True, temperature=0.7, top_p=0.95)
gsm8k_reader_cfg = dict(input_columns=['question'], output_column='answer')

gsm8k_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            begin=dict(
                role='SYSTEM',
                prompt='You are a world-class AI system, capable of complex reasoning and reflection. Reason through the query inside <thinking> tags, and then provide your final response inside <output> tags. If you detect that you made a mistake in your reasoning at any point, correct yourself inside <reflection> tags.'
            ),
            round=[
                dict(role='HUMAN', prompt='{question}\nPlease reason step by step, and put your final answer within \\boxed{}.If you use code to solve problem, you must execute your code to get an answer for responding and put your final answer within \\boxed{}.'),
            ],
        )),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=SCInferencer, max_out_len=4096,generation_kwargs=generation_kwargs,infer_type='sc',sc_size=1))

gsm8k_eval_cfg = dict(evaluator=dict(type=MATHEvaluator, version='v2'),
                      pred_postprocessor=dict(type=math_postprocess_v2),
                      dataset_postprocessor=dict(type=gsm8k_dataset_postprocess),sc_size=1)

gsm8k_datasets = [
    dict(
        abbr='gsm8k',
        type=GSM8KDataset,
        path='opencompass/gsm8k',
        reader_cfg=gsm8k_reader_cfg,
        infer_cfg=gsm8k_infer_cfg,
        eval_cfg=gsm8k_eval_cfg)
]
