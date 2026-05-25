from character_counter import analyze_text
from data_extractor import parse_annotator_raw

test_notes = """
Note from reviewer.one@linguistics.org: The translation for [GREETING] should definitely include ẹ kàárọ̀. 
Also, check with qa_team@institute.edu about the [SYNTAX_ERROR] near the word ọ̀pákùtẹ̀lẹ̀ and submit your work
before 23/10/2026.
"""

extractor = parse_annotator_raw(test_notes)
tag_list = extractor["tags"]

tag_string = "".join(tag_list)

extracted_token = analyze_text(tag_string)



print("Extracted Dictionary: ")
print(extractor)
print("\n==========\n")

print("Character count for the extracted dictionary: ")
print(extracted_token)
print("\n==========\n")