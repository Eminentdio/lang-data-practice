import pandas as pd

df = pd.read_csv("../data/raw/translations.csv")

cleaned_dataset = df[df['target_text'].notna()]
filtered_dataset = cleaned_dataset[cleaned_dataset['annotator_score'] >= 4]

output_file = filtered_dataset.to_csv("../data/processed/high_quality_corpus.csv", index=False)

print("Dataset Audit Complete")
print(f"Original rows: {len(df)}")
print(f"Cleaned rows: {len(filtered_dataset)}")
print("\nSuccess! High quality corpus saved to disk.")

