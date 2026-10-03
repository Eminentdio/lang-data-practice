import spacy

def analyze_morphology(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    

    print(f"{'Token':<15} | {'Lemma':<12} | {'POS':<6} | Morphology Features")
    print("-" * 75)
    
    for token in doc:
        if not token.is_punct:
            morph_dict = token.morph.to_dict()
            morph_str = ", ".join(f"{k}={v}" for k, v in morph_dict.items()) if morph_dict else "None"
            print(f"{token.text:<15} | {token.lemma_:<12} | {token.pos_:<6} | {morph_str}")

    return token.text, token.lemma_, token.pos_, morph_dict


sample_text = input("Enter text to analyze: ")
analyze_morphology(sample_text)