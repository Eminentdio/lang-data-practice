import pandas as pd

df = pd.read_csv("../data/raw/translations.csv")
print("Original Dataset:")
print(df)
print("\n-------------------------\n")

print("Dataset Audit: ")
df.info()

print("\n-------------------------\n")

clean_df = df[df['target_text'].notna()]
print(clean_df)
print("\n-------------------------\n")