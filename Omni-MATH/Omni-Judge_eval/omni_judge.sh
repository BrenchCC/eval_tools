export CUDA_VISIBLE_DEVICES=0

OUTFILE="final_results/xDAN-L3-Agentic-Reflection-Math-0919-liger-Instruct-v3-e3-final.jsonl"

python3 Omni_Judge.py \
    -i gen_results/xDAN-L3-Agentic-Reflection-Math-0919-liger-Instruct-v3-e3-sorted.jsonl \
    -o  $OUTFILE \
    -m /data/vayu/train/models/Omni-Judge



python3 get_result.py \
    -i $OUTFILE \

python3 ./detailed_evaluation/domain_specific_evaluation.py \
    --input_file $OUTFILE \

python3 ./detailed_evaluation/difficulty_specific_evaluation.py \
    --input_file $OUTFILE \
