import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse
import json
import pdb
from tqdm import tqdm
import os

def get_batch_responses(
    contexts,
    tokenizer,
    model,
    terminators,
    batch_size=8,
    max_new_tokens=300,
):
    total_pred = []
    total_input_ids = []
    tokenizer.padding_side = "left"

    batch = []
    for index in range(len(contexts)):
        batch.append(contexts[index])
        if len(batch) == batch_size or index == len(contexts) - 1:
            # tokenize
            model_inputs = tokenizer(batch, padding=True, return_tensors="pt")
            batch_input_ids = model_inputs["input_ids"].to(model.device)
            batch_attention_mask = model_inputs["attention_mask"].to(model.device)

            with torch.no_grad():
                batch_pred = model.generate(
                    batch_input_ids,
                    attention_mask=batch_attention_mask,
                    do_sample=False,
                    num_return_sequences=1,
                    max_new_tokens=max_new_tokens,
                ).cpu().tolist()
            
            total_pred.extend(batch_pred)
            total_input_ids.extend(batch_input_ids.cpu().tolist())
            batch = []

    responses = []
    for pred, input_ids in zip(total_pred, total_input_ids):
        # post-process
        assert pred[:len(input_ids)] == input_ids
        pred = pred[len(input_ids):]
        for terminator in terminators:
            if terminator in pred:
                pred = pred[:pred.index(terminator)]
        response = tokenizer.decode(pred, skip_special_tokens=True)
        responses.append("## Student Final Answer\n" + response.strip())

    return responses


def main(args):
    # Load the model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path, 
        device_map="auto", 
        torch_dtype=torch.bfloat16, 
    )
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_path,
        trust_remote_code=True,
        use_fast=True
    )

    # Set terminators for decoding
    terminators = [
        tokenizer.eos_token_id,
        tokenizer.convert_tokens_to_ids("<|eot_id|>")
    ]

    # Read input data
    inputs = []
    with open(args.in_file) as f:
        for line in f.readlines():
            inputs.append(json.loads(line))

    # Check existing out-file to get the highest ID
    max_id = -1
    if os.path.exists(args.out_file):
        with open(args.out_file, 'r') as f:
            for line in f:
                data = json.loads(line)
                max_id = max(max_id, data['id'])

    # Filter input data to only process new entries (those with id > max_id)
    new_inputs = [d for d in inputs if d['id'] > max_id]

    if not new_inputs:
        print("No new entries to process.")
        return

    id = [d['id'] for d in new_inputs]
    questions = [d['problem'] for d in new_inputs]
    reference_answers = [d['answer'] for d in new_inputs]
    student_solutions = [d['model_generation'] for d in new_inputs]

    # Prepare contexts for each input
    contexts = []
    for question, reference_answer, student_solution in zip(questions, reference_answers, student_solutions):
        formatted_context = tokenizer.get_context(question, reference_answer, student_solution)
        contexts.append(formatted_context)

    # Process batches and write results to file after each batch
    with open(args.out_file, 'a') as f:
        with tqdm(total=len(contexts), desc="Processing batches", unit="batch") as pbar:
            for i in range(0, len(contexts), args.batch_size):
                batch_contexts = contexts[i:i + args.batch_size]
                batch_questions = questions[i:i + args.batch_size]
                batch_reference_answers = reference_answers[i:i + args.batch_size]
                batch_student_solutions = student_solutions[i:i + args.batch_size]
                batch_inputs = new_inputs[i:i + args.batch_size]

                # Generate responses for the batch
                omni_judge_result = get_batch_responses(batch_contexts, tokenizer, model, terminators)

                # Write the batch results to the output file
                for (q, r, s, o, d) in zip(batch_questions, batch_reference_answers, batch_student_solutions, omni_judge_result, batch_inputs):
                    f.write(json.dumps({
                        'id': d['id'],
                        'domain': d['domain'],
                        'difficulty': d['difficulty'],
                        'source': d['source'],
                        'problem': q,
                        'answer': r,
                        'model_generation': s,
                        'omni_judge': o
                    }) + '\n')

                # Update progress bar after processing the batch
                pbar.update(len(batch_contexts))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Omni-Judge")
    parser.add_argument("-i", "--in-file", type=str, required=True, help="Input file path")
    parser.add_argument("-m", "--model-path", type=str, required=True, help="Model path")
    parser.add_argument("-o", "--out-file", type=str, required=True, help="Output file path")
    parser.add_argument("-b", "--batch-size", type=int, default=8, help="Batch size for processing")

    args = parser.parse_args()
    main(args)
