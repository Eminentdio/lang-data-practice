import re

def parse_annotator_raw(raw_data):
    email_pattern = r"[\w.-]+@[\w.-]+\.[a-zA-Z0-9_]{2,}"
    found_emails = re.findall(email_pattern, raw_data)

    dates_pattern = r"\d{2}/\d{2}/\d{4}"
    found_dates = re.findall(dates_pattern, raw_data)

    tonal_pattern = r"\b\w*[áàẹọṣíìúùóò]\w*\b"
    tonal_words = re.findall(tonal_pattern, raw_data)
    
    enclosed_pattern = r"\[\w+\]"
    enclosed_word = re.findall(enclosed_pattern, raw_data)

    return {
        "email": found_emails,
        "date" : found_dates,
        "tones" : tonal_words,
        "tags" : enclosed_word
    }
