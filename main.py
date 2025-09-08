from stats import get_number_of_words, get_charachter_number, sort_character
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = args[1]
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}")
    text = get_book_text(book_path)
    print(f"----------- Word Count ----------\nFound {get_number_of_words(text)} total words")
    print(f"--------- Character Count -------")
    for dict_ in sort_character(get_charachter_number(text)):
        char = dict_["char"]
        val = dict_["num"]
        if char.isalpha():
            print(f"{char}: {val}")
    print("============= END ===============")
main()
