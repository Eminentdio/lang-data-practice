input_text = "Àwọn àpólà méjéèjì yẹn ni àkòrí wa " \
"kó sínú nítorí pé ohun tí ó ń mú ìgbéyàwó gbópọn nìyẹn. " \
"Nínú ìgbéyàwó nígbà tí kò bá sí ìfẹ́  àti àánú wàyìí ọkọ àti " \
"ìyàwó náà ti kúrò ní lọ́kọláyà, wọ́n kàn ń tanra wọn jẹ lásán ni " \
"nítorí pé ohun tí ó jẹ́ ọ̀pákùtẹ̀lẹ̀ ìgbéyàwó wọn ni wọ́n ti ṣàfẹ́kù " \
"rẹ̀ yẹn èyí gan-an sì ni ìdí tí Ọlọ́run fi sọ pé kí wọ́n fẹ́ra. "


tokenized_text = input_text.split()

print("====Source texts====")
print(tokenized_text)

char_frequency = {}

for char in input_text.lower():
    if char.isalpha():

        if char in char_frequency:
            char_frequency[char] = char_frequency[char] + 1
        else:
            char_frequency[char] = 1

print("====Distributed Character====")
print(char_frequency)