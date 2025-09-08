def get_number_of_words(string):
    return len(string.split())

def get_charachter_number(string):
    character_dict = {}
    for char in string:
        char = char.lower()
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict

def sort_character(dict_of_character):
    list_of_dict = []
    for key,value in dict_of_character.items():
        list_of_dict.append({"char":key, "num": value})
    list_of_dict.sort(key=sort_on,reverse=True)
    return list_of_dict

def sort_on(item):
    return item["num"]
