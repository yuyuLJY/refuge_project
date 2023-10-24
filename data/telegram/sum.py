import pandas as pd
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from rouge_score import rouge_scorer


data = pd.read_csv('scrape.telegram_forwardsGT30_TokensGT100.csv')


model_name1 = 'lljllll2219/uk-mt5-base-xlsum-v3'
tokenizer1 = AutoTokenizer.from_pretrained(model_name1)
model1 = AutoModelForSeq2SeqLM.from_pretrained(model_name1)

model_name2 = 'csebuetnlp/mT5_multilingual_XLSum'
tokenizer2 = AutoTokenizer.from_pretrained(model_name2)
model2 = AutoModelForSeq2SeqLM.from_pretrained(model_name2)

# 定义生成摘要的函数
def generate_summary(text, tokenizer, model):
    inputs = tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


data['pre_sum'] = data['messageText'].map(lambda x: generate_summary(x, tokenizer1, model1))
data['Tar_sum'] = data['messageText'].map(lambda x: generate_summary(x, tokenizer2, model2))

def calculate_rouge(pre_sum, tar_sum):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(tar_sum, pre_sum)
    return {
        'rouge1': scores['rouge1'].fmeasure,
        'rouge2': scores['rouge2'].fmeasure,
        'rougeL': scores['rougeL'].fmeasure,
    }


rouge_scores = data.apply(lambda row: calculate_rouge(row['pre_sum'], row['Tar_sum']), axis=1)
rouge_df = pd.DataFrame(list(rouge_scores))


new_data = pd.DataFrame({
    'messageText': data['messageText'],
    'pre_sum': data['pre_sum'],
    'Tar_sum': data['Tar_sum'],
    'rouge1': rouge_df['rouge1'],
    'rouge2': rouge_df['rouge2'],
    'rougeL': rouge_df['rougeL'],
})


new_data.to_csv('summary_results.csv', index=False)

