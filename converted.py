import json

def convert_label_to_integer(label):
    if label == "entailment":
        return 0
    elif label == "non-entailment":
        return 2
    else:
        return None

def process_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as input_file:
        with open(output_file, 'w', encoding='utf-8') as output_file:
            for line in input_file:
                data = json.loads(line)
                premise = data["sentence1"]
                hypothesis = data["sentence2"]
                label = convert_label_to_integer(data["gold_label"])
                
                if label is not None:
                    formatted_data = {
                        "premise": premise,
                        "hypothesis": hypothesis,
                        "label": label
                    }
                    output_file.write(json.dumps(formatted_data) + '\n')

# Replace 'input.jsonl' and 'output.jsonl' with your actual file names
process_jsonl('data.jsonl', 'output.jsonl')
