from stats import get_num_of_words
from stats import get_num_of_characters
import sys
def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def sort_on(dict):
    return dict["count"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_of_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_of_book}...")
    print("----------- Word Count ----------")
    text_from_book = get_book_text(path_of_book)
    print(f"Found {get_num_of_words(text_from_book)} total words")
    print("--------- Character Count -------")
    num_of_ch_count = get_num_of_characters(text_from_book)
    list_of_dict = []
    for ch in num_of_ch_count:
        if ch.isalpha():
            list_of_dict.append({"character":ch,"count":num_of_ch_count[ch]})
    list_of_dict.sort(reverse=True, key=sort_on)
    for ch_dict in list_of_dict:
        print(f"{ch_dict["character"]}: {ch_dict["count"]}")
main()
