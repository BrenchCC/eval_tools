from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer,SCInferencer
from opencompass.datasets import IFEvalDataset, IFEvaluator
generation_kwargs = dict(do_sample=True, temperature=0.7, top_p=0.95)
ifeval_reader_cfg = dict(
    input_columns=['prompt'], output_column='reference')

ifeval_infer_cfg = dict(
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
                prompt='{prompt}'),
        ])),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=SCInferencer, max_out_len=1025,generation_kwargs=generation_kwargs,infer_type='sc',sc_size=1))

ifeval_eval_cfg = dict(
    evaluator=dict(type=IFEvaluator),
    pred_role='BOT',
    sc_size=1
)

ifeval_datasets = [
    dict(
        abbr='IFEval',
        type=IFEvalDataset,
        path='data/ifeval/input_data.jsonl',
        reader_cfg=ifeval_reader_cfg,
        infer_cfg=ifeval_infer_cfg,
        eval_cfg=ifeval_eval_cfg)
]
