from mmengine import read_base

from opencompass.openicl import ZeroRetriever
from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import FixKRetriever
from opencompass.openicl.icl_inferencer import GenInferencer,SCInferencer
from opencompass.openicl.icl_evaluator import AccwithDetailsEvaluator
from opencompass.datasets import MMLUDataset
from opencompass.utils.text_postprocessors import first_option_postprocess, last_option_postprocess

# None of the mmlu dataset in huggingface is correctly parsed, so we use our own dataset reader
# Please download the dataset from https://people.eecs.berkeley.edu/~hendrycks/data.tar

with read_base():
    from .mmlu_all_sets import mmlu_all_sets
    from .shot import data_dict

mmlu_reader_cfg = dict(
    input_columns=['input', 'A', 'B', 'C', 'D'],
    output_column='target',
    train_split='dev')

mmlu_datasets = []
for _name in mmlu_all_sets:
    prompt = data_dict[_name]
    rounds = []
    # 遍历 prompt 中的每一对问答
    for i in range(1, len(prompt)):
        rounds.append(
            dict(
                role='HUMAN',
                prompt=prompt[i][0],
            )
        )  # 防止超出索引范围
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
                begin=dict(
                    role='SYSTEM',
                    prompt=f'You are an expert in {_name.replace("_", " ")}.{prompt[0]}'
                ),
                round=rounds + [
                    dict(
                        role='HUMAN',
                        prompt=f'''Q: {{input}}\n(A) {{A}} (B) {{B}} (C) {{C}} (D) {{D}}\nA: Let's think step by step.'''
                    )
                ],
            ),
        ),
        retriever=dict(type=ZeroRetriever),
        #inferencer=dict(type=GenInferencer,max_out_len=512),
        #inferencer=dict(type=SCInferencer, max_out_len=512, do_sample=True,temperature=1.0,min_p=0.1,infer_type='sc', sc_size = 8)
        inferencer=dict(type=SCInferencer, max_out_len=512, do_sample=True,temperature=0.7,top_k=50,infer_type='sc', sc_size = 8)
    )

    mmlu_eval_cfg = dict(
        evaluator=dict(type=AccwithDetailsEvaluator),
        pred_postprocessor=dict(type=last_option_postprocess, options='ABCD'),
        sc_size=8
)

    mmlu_datasets.append(
        dict(
            abbr=f'lukaemon_mmlu_{_name}',
            type=MMLUDataset,
            path='opencompass/mmlu',
            name=_name,
            reader_cfg=mmlu_reader_cfg,
            infer_cfg=mmlu_infer_cfg,
            eval_cfg=mmlu_eval_cfg,
        ))

del _name
