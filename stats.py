def get_num_of_words(content):
    return len(content.split())
    
def get_num_of_characters(content):
    lower_content = content.lower()
    letter_dict = {}
    for ch in lower_content:
        if ch in letter_dict:
            letter_dict[ch] += 1
        else:
            letter_dict[ch] = 1
    return letter_dict
    