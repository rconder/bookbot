
def sort_on(dict):
    return dict['count']

def main():
    letter_dict ={} 
    with open("books/frankenstein.txt") as f:
        file_contents= f.read()
        listofwords = file_contents.split()
        for word in listofwords:
            for letter in word.lower():
                if letter.isalpha():
                    if  letter in letter_dict:
                        letter_dict[letter] += 1
                    else:
                        letter_dict[letter] = 1
    letter_dict_list = []
    for letter, count in letter_dict.items():
        letter_dict_list.append({'letter': letter, 'count': count})
    letter_dict_list.sort(reverse=True, key=sort_on) 
    
    print("--- Begin report of books/frankenstein.txt ---")
    for item in letter_dict_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    print("--- End of report ---")

main()