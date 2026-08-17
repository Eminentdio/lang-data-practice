import pandas as pd
import spacy

# ____load spaCy model____
nlp = spacy.load("en_core_web_sm")

# _____inject raw corpus___

raw_corpus_df = pd.read_csv("../data/raw/unfiltered_web_corpus.csv")

def audit_text_quality(text):
    """
    Analyzes syntactic quality using POS tags and dependency relations.
    Returns: (is_valid: bool, rejection_reason: str)
    """
    doc= nlp(str(text))
    total_tokens = len(doc)


    # ___Rule 0: Minimum lenght check___
    
    if total_tokens < 4:
        return False, "TOO_SHORT"

    # ___counting POS distribution___

    pos_counts = {
        "NOUN_LIKE": sum(1 for t in doc if t.pos_ in ("NOUN", "PROPN", "ADJ")),
        "VERB": sum(1 for t in doc if t.pos_ in ("VERB", "AUX")),
        "PUNCT_SYM": sum(1 for t in doc if t.pos_ in ("PUNCT", "SYM"))  
    }

    # Rule 1: Noise/Symbol Threshold(over 25% punctuation and symbols)
    if (pos_counts["PUNCT_SYM"] / total_tokens) > 0.25:
        return False, "HIGH_SYMBOL_NOISE"

    # Rule 2: Complete Predicate Check (Must contain at least one governing verb)
    has_root_verb = any(t.pos in ("VERB", "AUX") and t.dep_ == "ROOT" for t in doc)
    if not has_root_verb or pos_counts["VERB"] == 0:
        return False, "NO_VALID_PREDICATE"
    

    # Rule 3: Keyword Stuffing / SEO Spam Check
    noun_ratio = pos_counts["NOUN_LIKE"] / total_tokens
    if noun_ratio > 0.80:
        return False, "KEYWORD_STUFFED_SPAM"
    
    return True, "PASSED"


    # _____Apply audit across the Dataframe_____

audit_results = [audit_text_quality(text) for text in raw_corpus_df["raw_text"]]
raw_corpus_df["is_valid"] = [res[0] for res in audit_results]
raw_corpus_df["rejection_reason"] = [res[1] for res in audit_results]

# ______Split clean data from rejected logs_______

clean_corpus_df = raw_corpus_df[raw_corpus_df["is_valid"]].drop(columns=["is_valid", "rejection_reason"])
rejected_corpus_df = raw_corpus_df[~raw_corpus_df["is_valid"]]


# ___Export results___

clean_corpus_df.to_csv("../data/processed/clean_corpus.csv", index=False)
rejected_corpus_df.to_csv("../data/processed/rejected_report.csv", index=False)

print("--- CORPUS QUALITY AUDIT COMPLETE ---")
print(f"Total rows processed : {len(raw_corpus_df)}")
print(f"Clean rows saved     : {len(clean_corpus_df)}")
print(f"Rejected rows flagged: {len(rejected_corpus_df)}\n")
print("Rejection Breakdown:")
print(rejected_corpus_df["rejection_reason"].value_counts().to_string())