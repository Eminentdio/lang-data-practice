def analyze_text(raw_text):
    """
    This function will take a raw string of texts, convert
    it to lowercase, and a dictionary of character frequencies,
    ignoring number and punctuations.

    C:\Users\User\.local\bin 

     Next: Run claude --help to get started

    """

    char_frequency = {}             # an empty dictionary to hold the character frequencies

    for char in raw_text.lower():   # loop through the raw text and convert to lowercase

        if char.isalpha():          # check if the character are letters
            if char in char_frequency:       # if the character is already in our dictionary add 1 to the count
                char_frequency[char] = char_frequency[char] + 1
            else:       # if we have not seen this character yet, add it to the dictionary bucket with a count of 1
                char_frequency[char] = 1
        
    return char_frequency