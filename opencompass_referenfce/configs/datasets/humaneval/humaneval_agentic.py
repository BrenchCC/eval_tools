# THIS SHALL ALSO BE DEPRECATED
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.datasets import HumanevalDataset, HumanEvalEvaluator, humaneval_postprocess_v2_agentic

humaneval_reader_cfg = dict(
    input_columns=['prompt'], output_column='task_id', train_split='test')

# TODO: allow empty output-column
humaneval_infer_cfg = dict(
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
            dict(
                role='HUMAN',
                prompt='''Complete the following python code:\n{prompt}\nMake sure put the whole finished python code inside <output> tag,using the markdown form.
                Your response must contain this content as follow:
                <thinking>{content}</thinking>
                <reflection>{content}</reflection>
                <output>```python {your code}```</output>'''
            ),
        ])),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer))

humaneval_eval_cfg = dict(
    evaluator=dict(type=HumanEvalEvaluator),
    pred_role='BOT',
    k=[1, 10, 100],  # the parameter only for humaneval
    pred_postprocessor=dict(type=humaneval_postprocess_v2_agentic),
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
