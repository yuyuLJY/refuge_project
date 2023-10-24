import pandas as pd


df = pd.read_csv('summary_results.csv')

rouge1_mean = df['rouge1'].mean()
rouge2_mean = df['rouge2'].mean()
rougeL_mean = df['rougeL'].mean()


print(f'rouge1:{rouge1_mean}')
print(f'rouge2: {rouge2_mean}')
print(f'rougeL: {rougeL_mean}')