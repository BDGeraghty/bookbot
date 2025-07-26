from curses.ascii import isalpha
from stats import get_num_words, get_chars_dict
import sys


def main():

    book_path = ""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        book_path = sys.argv[1]
        print(f"Book Title: {book_path}")
    
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    #char_dict = text_to_charcount(book_text)
    ##print(char_dict)
    sorted_chars_dict = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)
    print("--------- Character Count -------")
    for char, count in sorted_chars_dict:
        if isalpha(char):
            print(f"{char}: {count}")
    print("============= END ===============")
   
def get_book_text(path):
    with open(path) as f:
        return f.read()

if __name__ == "__main__":
    main()


