from mmengine.config import read_base
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.openicl.icl_evaluator import AccEvaluator,AccwithDetailsEvaluator
from opencompass.datasets import MMLUDataset
from opencompass.utils.text_postprocessors import match_answer_pattern, last_option_postprocess

with read_base():
    from .mmlu_all_sets import mmlu_all_sets
    from .shot import data_dict

# None of the mmlu dataset in huggingface is correctly parsed, so we use our own dataset reader
# Please download the dataset from https://people.eecs.berkeley.edu/~hendrycks/data.tar

QUERY_TEMPLATE = """
Answer the following multiple choice question. The last line of your response should be of the following format: 'The answer is ($LETTER)' (without quotes) where LETTER is one of ABCD. Think step by step before answering.
Q:{input}
(A) {A} (B) {B} (C) {C} (D) {D} \n
"""

mmlu_reader_cfg = dict(
    input_columns=['input', 'A', 'B', 'C', 'D'],
    output_column='target',
    train_split='dev')

mmlu_datasets = []
for name in mmlu_all_sets:
    prompt=data_dict[name]
    rounds = []
    # 遍历 prompt 中的每一对问答
    for i in range(1, len(prompt)):
        rounds.append(
            dict(
                role='HUMAN',
                prompt='''Answer the following multiple choice question. The last line of your response should be of the following format: 'The answer is ($LETTER)' (without quotes) where LETTER is one of ABCD. Think step by step before answering.\n'''+prompt[i][0],
            )
        )
        rounds.append(
            dict(
                role='BOT',
                prompt=f'A: {prompt[i][1]}',
            )
        )

    mmlu_infer_cfg = dict(
        prompt_template=dict(
            type=PromptTemplate,
            template=dict(
		begin=dict(role='SYSTEM', fallback_role='HUMAN',prompt=f'You are an expert in {name.replace("_", " ")}.{prompt[0]}'),
                round=rounds+[
                    dict(role='HUMAN', prompt=QUERY_TEMPLATE),
                ],
            ),
        ),
        retriever=dict(type=ZeroRetriever),
        inferencer=dict(type=GenInferencer),
    )

    mmlu_eval_cfg = dict(
        evaluator=dict(type=AccwithDetailsEvaluator),
        pred_postprocessor=dict(type=last_option_postprocess, options='ABCD'))

    mmlu_datasets.append(
        dict(
            abbr=f'lukaemon_mmlu_{name}',
            type=MMLUDataset,
            path='opencompass/mmlu',
            name=name,
            reader_cfg=mmlu_reader_cfg,
            infer_cfg=mmlu_infer_cfg,
            eval_cfg=mmlu_eval_cfg,
        ))
