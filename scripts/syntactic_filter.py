import pandas as pd
import spacy
from pathlib import Path

nlp = spacy.load("en_core_web_sm")
project_root = Path(__file__).resolve().parents[1]
processed_dir = project_root / "data" / "processed"
df = pd.read_csv(processed_dir / "cnn_politics_stories_cleaned.csv")

def audit_text_quality(text):
    """
    Analyses syntactic quality using POS tags and dependency relation.
    Returns: (is_valid: bool, rejection_reason: str)
    """
    doc = nlp(str(text))
    total_tokens = len(doc)

    # Rule 0: Minimum length check
    if total_tokens < 4:
        return False, "TOO SHORT"

    # Count POS distribution
    pos_counts = {
        "NOUN_LIKE": sum(1 for t in doc if t.pos_ in ("NOUN", "PROPN", "ADJ")),
        "VERBS": sum(1 for t in doc if t.pos_ in ("VERB", "AUX")),
        "PUNCT_SYM": sum(1 for t in doc if t.pos_ in ("PUNCT", "SYM")),
    }

    # Rule 1: Noise/Symbol Threshold (over 25% punctuuations or symbols)
    if pos_counts["PUNCT_SYM"] / total_tokens > 0.25:
        return False, "HIGH_SYMBOL_NOISE"

    # Rule 2: Complete predicate check (at least one governing verb)
    has_root_verb = any(t.pos_ in ("VERB", "AUX") and t.dep_ == "ROOT"  for t in doc)
    if not has_root_verb or pos_counts["VERBS"] == 0:
        return False, "NO_VALID_PREDICATE"

    # Rule 3: Keyword stuffing or SEO spam check (Over 80% nouns/adjectives)
    noun_adj_ratio = pos_counts["NOUN_LIKE"] / total_tokens
    if noun_adj_ratio > 0.80:
        return False, "KEYWORD_STUFFED_SPAM"

    return True, "PASSED"

# Apply audit across the dataframe
audit_results = [audit_text_quality(text) for text in df["text"]]
df["is_valid"] = [res[0] for res in audit_results]
df["rejection_reason"] = [res[1] for res in audit_results]

# Split clean data from rejection logs
clean_df = df[df["is_valid"]].drop(columns=["is_valid", "rejection_reason"])
rejection_logs = df[~df["is_valid"]]

# Save results to CSV
clean_df.to_csv(processed_dir / "cnn_politics_stories_cleaned_filtered.csv", index=False)
rejection_logs.to_csv(processed_dir / "cnn_politics_stories_rejection_logs.csv", index=False)

# Summary

print("--- CORPUS QUALITY AUDIT COMPLETE ---")
print(f"Total rows processed : {len(df)}")
print(f"Clean rows saved     : {len(clean_df)}")
print(f"Rejected rows flagged: {len(rejection_logs)}\n")
print("Rejection Breakdown:")
print(rejection_logs["rejection_reason"].value_counts().to_string())






# ====== FOR TESTING PURPOSES ======

# import spacy
# nlp = spacy.load("en_core_web_sm")

# test_strings = [
#     "cheap shoes sale discount online buy footwear",  # Should fail: KEYWORD_STUFFED_SPAM
#     "Under the table near the entrance.",            # Should fail: NO_VALID_PREDICATE
#     "$$$ *** >>> ERROR 404 ??? !!!",                  # Should fail: HIGH_SYMBOL_NOISE
#     "Hi",                                            # Should fail: TOO_SHORT
#     "The linguist analyzes corpus data with spaCy."   # Should pass: PASSED
# ]

# for text in test_strings:
#     doc = nlp(text)
#     total = len(doc)
#     has_root_verb = any(t.pos_ in ("VERB", "AUX") and t.dep_ == "ROOT" for t in doc)
#     noun_ratio = sum(1 for t in doc if t.pos_ in ("NOUN", "PROPN", "ADJ")) / max(total, 1)
#     punct_ratio = sum(1 for t in doc if t.pos_ in ("PUNCT", "SYM")) / max(total, 1)
    
#     print(f"\nText: {text}")
#     print(f"Tokens: {total} | Has Root Verb: {has_root_verb} | Noun Ratio: {noun_ratio:.2f} | Punct Ratio: {punct_ratio:.2f}")

# ===== END OF TESTING ======